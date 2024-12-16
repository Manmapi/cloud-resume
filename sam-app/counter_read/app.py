import json

import boto3

client = boto3.client('dynamodb')

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

    return {
        "statusCode": 200,
        "body": json.dumps(response.get("Item")),
        "headers": {
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS"
        }
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
        response = client.update_item(
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
            "headers": {
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,OPTIONS"
            }
        }
    except Exception:
        return {
            "statusCode": 500,
            "headers" : {
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,OPTIONS"
            },
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
                })
            }
