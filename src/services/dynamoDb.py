import boto3
from dotenv import dotenv_values
from botocore.exceptions import ClientError
from ..config import config



dynamodb = boto3.resource(
    'dynamodb', 
    region_name=config.get("region_name"),
    aws_access_key_id=config.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=config.get('AWS_SECRET_ACCESS_KEY')
)


def dynamodb_handler(table_name):
    """
    Provides a DynamoDB table handler for CRUD operations.

    Args:
        table_name (str): The name of the DynamoDB table.

    Returns:
        DynamoDB table object.
    """
    try:
        table = dynamodb.Table(table_name)
        return table
    except ClientError as e:
        print(f"Error connecting to DynamoDB table: {e}")
        raise e
