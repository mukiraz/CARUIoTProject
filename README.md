# IoT Data Pipeline with AWS

## Overview
This project is designed to collect, process, store, and analyze data from IoT devices using AWS services. The architecture leverages various AWS services such as AWS AppSync, AWS Lambda, DynamoDB, AWS IoT Core, EventBridge, AWS Cognito, AWS Glue, Athena, and CloudWatch for a robust and scalable IoT data pipeline.

This project was specially created for the interview with CARU on 28.10.2024.

## Architecture
The main components of the architecture include:
- **ESP8266 IoT Devices:** Sends sensor data (e.g., temperature, humidity) to AWS IoT Core.
- **AWS IoT Core:** Manages the communication between IoT devices and AWS services using MQTT protocol.
- **AWS AppSync (GraphQL API):** Provides a GraphQL API to interact with the data.
- **AWS Lambda:** Processes the data coming from IoT devices and stores it in DynamoDB.
- **Amazon DynamoDB:** Stores the processed IoT data for analysis and querying.
- **AWS EventBridge:** Manages event-driven workflows and triggers actions based on incoming data.
- **Amazon Cognito:** Manages user authentication for secure access to the API.
- **AWS Glue and Athena:** Analyzes and queries the data stored in DynamoDB.
- **AWS CloudWatch:** Monitors the health of the system, logs data, and sets up alarms.
- **Amazon S3:** Stores logs, backup data, and other files.

## Prerequisites
- An AWS account.
- AWS CLI installed and configured.
- Node.js and AWS CDK installed for deploying the infrastructure.
- An ESP8266 device with internet connectivity.

## Project Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/iot-data-pipeline.git
   cd iot-data-pipeline


# IoT Data Pipeline with AWS

## Overview
This project is designed to collect, process, store, and analyze data from IoT devices using AWS services. The architecture leverages various AWS services such as AWS AppSync, AWS Lambda, DynamoDB, AWS IoT Core, EventBridge, AWS Cognito, AWS Glue, Athena, and CloudWatch for a robust and scalable IoT data pipeline.

## Architecture
The main components of the architecture include:
- **ESP8266 IoT Devices:** Sends sensor data (e.g., temperature, humidity) to AWS IoT Core.
- **AWS IoT Core:** Manages the communication between IoT devices and AWS services using MQTT protocol.
- **AWS AppSync (GraphQL API):** Provides a GraphQL API to interact with the data.
- **AWS Lambda:** Processes the data coming from IoT devices and stores it in DynamoDB.
- **Amazon DynamoDB:** Stores the processed IoT data for analysis and querying.
- **AWS EventBridge:** Manages event-driven workflows and triggers actions based on incoming data.
- **Amazon Cognito:** Manages user authentication for secure access to the API.
- **AWS Glue and Athena:** Analyzes and queries the data stored in DynamoDB.
- **AWS CloudWatch:** Monitors the health of the system, logs data, and sets up alarms.
- **Amazon S3:** Stores logs, backup data, and other files.

## Prerequisites
- An AWS account.
- AWS CLI installed and configured.
- Node.js and AWS CDK installed for deploying the infrastructure.
- An ESP8266 device with internet connectivity.

## Project Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/iot-data-pipeline.git
   cd iot-data-pipeline
   ```

2. Install dependencies:
   ```bash
   npm install -g aws-cdk
   python3 -m venv .env
   source .env/bin/activate
   pip install -r requirements.txt
   ```

3. Deploy the CDK stack:
   ```bash
   cdk bootstrap
   cdk deploy
   ```


### AWS IAM User Permissions
The following permissions were granted to the IAM user **CARU-IoTDeveloper** through three groups for managing the AWS resources in this project:

#### CARU-IoT-and-API-Management-Group:
| Permission | Description |
|------------|-------------|
| **AWSLambda_FullAccess** | Allows full management of AWS Lambda functions. Enables the user to create, update, delete, and invoke Lambda functions. |
| **AWSIoTFullAccess** | Grants full access to AWS IoT Core, including managing IoT things, certificates, and MQTT communication. |
| **AWSAppSyncAdministrator** | Provides administrative access to manage AWS AppSync GraphQL APIs, including creating, updating, and deleting API schemas. |
| **AmazonCognitoPowerUser** | Allows management of Amazon Cognito user pools, including creating and managing users and authentication settings. |

#### CARU-Data-and-Analytics-Group:
| Permission | Description |
|------------|-------------|
| **AmazonDynamoDBFullAccess** | Allows full access to DynamoDB, enabling the creation, reading, writing, and deletion of tables and items. |
| **AWSGlueServiceRole** | Allows management of AWS Glue jobs, crawlers, and data catalogs for ETL (Extract, Transform, Load) processes. |
| **AmazonAthenaFullAccess** | Grants full access to Athena for running queries and managing results. |
| **AmazonS3FullAccess** | Allows full access to Amazon S3 for managing buckets and objects. Useful for storing logs, backups, and other files. |

#### CARU-Logging-and-Monitoring-Group:
| Permission | Description |
|------------|-------------|
| **CloudWatchFullAccess** | Provides full access to AWS CloudWatch for monitoring and logging. Allows creating alarms, dashboards, and viewing logs. |
| **CloudWatchFullAccessV2** | Provides enhanced permissions for CloudWatch, including additional capabilities for log management and monitoring. |
| **AmazonEventBridgeFullAccess** | Provides full access to manage EventBridge rules and events, allowing the user to create and modify rules for event-driven workflows. |
| **AWSLambdaBasicExecutionRole** | Provides basic execution permissions for AWS Lambda functions, including writing logs to CloudWatch. |
| **AWSLambdaVPCAccessExecutionRole** | Allows Lambda functions to access resources within a VPC. Necessary for Lambda functions that need to interact with resources inside a VPC. |
| **IAMUserChangePassword** | Allows IAM users to change their own password, which is useful for managing user credentials securely. |


## How to Use
1. **Deploying IoT Devices:**
   - Configure your ESP8266 devices to send data to the AWS IoT Core using MQTT.
   - Use the provided `mqtt-config.json` file to configure the MQTT topics and credentials.

2. **Interacting with the API:**
   - Use the provided `graphql/queries.graphql` and `graphql/mutations.graphql` files to interact with the AppSync GraphQL API.
   - Authentication is required using Amazon Cognito to access the API.

3. **Analyzing Data with Athena:**
   - Use AWS Glue to create a data catalog for DynamoDB.
   - Run SQL queries in Amazon Athena to analyze the IoT data.

4. **Monitoring the System:**
   - Use AWS CloudWatch to monitor logs from Lambda functions, IoT Core, and EventBridge events.
   - Set up CloudWatch alarms for critical metrics.

## Important Notes
- **Security:** Ensure that sensitive information such as API keys and access tokens are kept secure and not exposed in the source code.
- **Costs:** Be aware that using these AWS services may incur charges. Monitor your usage in the AWS Billing Dashboard.

## Contributing
Feel free to open issues or submit pull requests to improve this project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



### Özellikler:
- **Overview:** Projenin genel yapısını ve hangi AWS servislerini kullandığını açıklar.
- **Architecture:** Proje bileşenlerinin genel tanımını yapar.
- **Prerequisites ve Setup:** Projenin yerel ortamda çalıştırılabilmesi için gereken ön koşulları ve kurulum adımlarını açıklar.
- **IAM Permissions:** Projede kullanılan her bir izin ve bu iznin ne işe yaradığı hakkında kısa bir açıklama içerir.
- **How to Use:** Uygulamanın nasıl kullanılacağını ve ana adımları özetler.
- **Important Notes:** Güvenlik ve maliyet konularına dikkat çeker.
- **Contributing ve License:** Projeye katkıda bulunma ve lisans bilgilerini içerir.

