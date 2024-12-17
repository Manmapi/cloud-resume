# Cloud Resume Challenge

## Overview
This project demonstrates the use of **AWS services** to host a highly available, scalable, and fully serverless application. The architecture combines multiple AWS offerings to deliver a cost-effective, reliable, and efficient solution.

## AWS Services Used
- **AWS Lambda**: Executes backend logic without requiring server management.
- **Amazon S3**: Hosts static website content.
- **Amazon DynamoDB**: Provides a managed NoSQL database for data persistence.
- **Amazon API Gateway**: Routes client requests to AWS Lambda via managed APIs.
- **Amazon CloudFront**: Optimizes content delivery using a global Content Delivery Network (CDN).
- **Amazon Route 53**: Manages DNS routing for traffic.
- **AWS Systems Manager Parameter Store**: Securely stores and retrieves configuration variables.

## Architecture Diagram
*TODO: Add architecture diagram here.*

## Features
- **Serverless Architecture**: Eliminates the need for infrastructure management.
- **High Availability**: Ensures reliability through AWS-managed services.
- **Scalability**: Automatically scales to meet varying workloads.
- **Optimized Delivery**: Delivers static content globally with low latency using CloudFront.

## Project Components
1. **Static Website**
   - Hosted on **Amazon S3**.
   - Delivered globally using **Amazon CloudFront**.

2. **Backend Services**
   - RESTful APIs implemented using **AWS Lambda** and **Amazon API Gateway**.
   - **Amazon DynamoDB** for scalable data storage.

3. **Routing**
   - Traffic routing and DNS management via **Amazon Route 53**.

4. **Configuration Management**
   - Secure and centralized management of environment variables using **AWS Systems Manager Parameter Store**.

## Prerequisites
Before you begin, ensure the following:
- An AWS account with sufficient permissions.
- AWS CLI and AWS SAM CLI installed. Follow the installation guide [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html).

## Deployment
Follow these steps to deploy the project:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Manmapi/my_resume.git
   cd my_resume
   ``` 

2. **Configure Route 53 and ACM**
   - Purchase a domain using Route 53 or any other registrar.
   - Create a hosted zone in **Amazon Route 53**.
   - Use **AWS Certificate Manager (ACM)** to verify the domain you intend to use.

3. **Set Up Environment Variables with Systems Manager Parameter Store**
   - Create the following parameters:
     - `/my_cv/acm_certificate_arn`
     - `/my_cv/bucket_name`
     - `/my_cv/domain_name`
     - `/my_cv/hosted_zone_id`

4. **Set Up AWS SAM**
   - Validate the SAM template:
     ```bash
     cd sam-app
     sam validate
     ```
   - Generate the build folder:
     ```bash
     sam build
     ```
   - Deploy the application using:
     ```bash
     sam deploy --guided
     ```

5. **Upload Static Content**
   - Update your bucket name in the `init_data.sh` file.
   - Upload the static website content to your S3 bucket:
     ```bash
     bash init_data.sh
     ```

## Future Enhancements
- Implement logging and monitoring with **AWS CloudWatch**.
- Automate CI/CD pipelines using **AWS CodePipeline**.
