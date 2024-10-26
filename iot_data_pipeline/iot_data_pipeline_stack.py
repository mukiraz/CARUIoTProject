from aws_cdk import (
    aws_dynamodb as dynamodb,
    aws_lambda as _lambda,
    aws_appsync as appsync,
    aws_iot as iot,
    aws_cognito as cognito,
    aws_iam as iam,
    Stack,
    RemovalPolicy
)
from constructs import Construct

class IotDataPipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # DynamoDB Tablosu
        device_data_table = dynamodb.Table(
            self, "DeviceDataTable",
            partition_key=dynamodb.Attribute(name="deviceId", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="timestamp", type=dynamodb.AttributeType.STRING),
            removal_policy=RemovalPolicy.DESTROY
        )

        # Lambda Fonksiyonu (Veri İşleme)
        data_processor_lambda = _lambda.Function(
            self, "DataProcessorLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("iot_data_pipeline/lambda"),
            environment={
                'DYNAMODB_TABLE_NAME': device_data_table.table_name
            }
        )

        # Lambda'ya DynamoDB erişim izni ekleyin
        device_data_table.grant_read_write_data(data_processor_lambda)

        # AppSync API Tanımı
        api = appsync.GraphqlApi(
            self, "DeviceDataApi",
            name="DeviceDataApi",
            definition=appsync.Definition.from_file("iot_data_pipeline/graphql/schema.graphql"),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(
                    authorization_type=appsync.AuthorizationType.USER_POOL,
                    user_pool_config={
                        "user_pool": cognito.UserPool(self, "UserPool")
                    }
                )
            )
        )

        # AppSync ve Lambda Entegrasyonu
        lambda_datasource = api.add_lambda_data_source(
            "LambdaDataSource", 
            data_processor_lambda
        )

        # GraphQL Mutasyonları için Resolver Tanımları
        lambda_datasource.create_resolver(
            id="CreateDeviceDataResolver",
            type_name="Mutation",
            field_name="createDeviceData"
        )