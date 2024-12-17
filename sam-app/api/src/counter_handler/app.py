import json
import os
import boto3

client = boto3.client('dynamodb')

RETURNED_HEADERS = {
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Allow-Origin": os.environ["ALLOWED_DOMAINS"],
    "Access-Control-Allow-Methods": os.environ["ALLOWED_HEADERS"]
}

def handle_get(event):
    queries = event.get("queryStringParameters") or {}
    key_name = queries.get("name")

    if not queries:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Missing `name` query parameter "
            })
        }

    response = client.get_item(
        TableName="CounterTable",
        Key={
            "name": {
                "S": key_name
            }
        }
    )
    item = response.get("Item")
    if not item:
        # Handle case row is not existed
        client.put_item(
            TableName="CounterTable",
            Item={
                "name": {
                    "S": key_name
                },
                "counted": {
                    "N": "1"
                }
            }
        )
        item = {
            "counted": {
                "N": "1"
            }
        }

    return {
        "statusCode": 200,
        "body": json.dumps(item),
        "headers": RETURNED_HEADERS
    }

def handle_post(event):
    queries = event.get("queryStringParameters") or {}
    key_name = queries.get("name")

    if not queries:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Missing `name` query parameter "
            })
        }
    try:
        _response = client.update_item(
            TableName="CounterTable",
            Key={
                "name": {
                    "S": key_name
                }
            },
            UpdateExpression="set counted = counted + :inc ",
            ExpressionAttributeValues={
                ":inc": {"N": "1"}
            }
        )
        return {
            "statusCode": 200,
            "headers": RETURNED_HEADERS
        }
    except Exception:
        return {
            "statusCode": 500,
            "headers" : RETURNED_HEADERS,
            "body": json.dumps({
                "message": "Has error when update counter"
            })

        }

def lambda_handler(event, context):
    method = event.get("httpMethod")
    match method:
        case "GET":
            return handle_get(event)
        case "POST":
            return handle_post(event)
        case _:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "Invalid Method"
                }),
                "headers": RETURNED_HEADERS
            }
