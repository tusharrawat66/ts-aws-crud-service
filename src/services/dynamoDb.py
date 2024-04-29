import boto3
from dotenv import dotenv_values
from botocore.exceptions import ClientError
from src.config import config



# boto3.setup_default_session(
#     region_name=config.get("AWS_DEFAULT_REGION"),
#     endpoint_url=config.get("LOCALSTACK_ENDPOINT")
# )



def dynamodb_handler(table_name):
    """
    Provides a DynamoDB table handler for CRUD operations.

    Args:
        table_name (str): The name of the DynamoDB table.

    Returns:
        DynamoDB table object.
    """

    # boto3.setup_default_session(profile_name='test')

    dynamodb = boto3.resource(
        'dynamodb',
        region_name='us-east-1',
        endpoint_url=config.get("LOCALSTACK_ENDPOINT"),
        aws_access_key_id='test',
        aws_secret_access_key='test'
        )
    

    print(f"AWS_DEFAULT_REGION:  {config.get('AWS_DEFAULT_REGION')}")
    print(f"AWS_ACCESS_KEY_ID:  {config.get('AWS_ACCESS_KEY_ID')}")
    print(f"AWS_SECRET_ACCESS_KEY:  {config.get('AWS_SECRET_ACCESS_KEY')}")
    print(f"TABLE_NAME:  {config.get('TABLE_NAME')}")
    print(f"LOCALSTACK_ENDPOINT:  {config.get('LOCALSTACK_ENDPOINT')}")


    try:
        table = dynamodb.Table(table_name)
        return table
    except ClientError as e:
        print(f"Error connecting to DynamoDB table: {e}")
        raise e



def create_table(dynamodb, table_name):
    """
    Creates a new DynamoDB table.

    Args:
        dynamodb (boto3.client): DynamoDB client.
        table_name (str): The name of the DynamoDB table to create.
    """
    try:
        response = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        print(f"Table '{table_name}' created.")
    except ClientError as e:
        print(f"Error creating table '{table_name}': {e}")
        raise e