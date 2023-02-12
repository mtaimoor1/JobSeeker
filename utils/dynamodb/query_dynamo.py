import sys
from botocore.exceptions import ClientError
from .dynamodb_connector import Connector
from boto3.dynamodb.conditions import Key
import logging


dynamo = Connector()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


class DynamoQuery:

    def __init__(self):
        self.con = dynamo.get_conn

    def list_tables(self):
        result = list()
        for record in list(self.con.tables.all()):
            result.append(record.name)
        return result

    def get_all_records(self, name):
        table = self.con.Table(name)
        try:
            response = table.scan()
        except ClientError as exception:
            return [exception.response["Error"]]
        result = response["Items"]
        while "LastEvaluatedKey" in response:
            response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
            result.extend(response["Items"])
        return result

    def query_table(self, table, job_title):
        table = self.con.Table(table)
        try:
            response = table.query(
                KeyConditionExpression=Key('job_title').eq(job_title)
            )
        except ClientError as exception:
            return [exception.response["Error"]]
        result = response['Items']
        while "LastEvaluatedKey" in response:
            response = table.query(
                KeyConditionExpression=Key('job_title').eq(job_title),
                ExclusiveStartKey=response["LastEvaluatedKey"]
            )
            result.extend(response["Items"])
        return result
