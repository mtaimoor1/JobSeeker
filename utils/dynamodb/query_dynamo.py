from .dynamodb_connector import Connector
from boto3.dynamodb.conditions import Key

dynamo = Connector()


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
        response = table.scan()
        result = response["Items"]
        while "LastEvaluatedKey" in response:
            response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
            result.extend(response["Items"])
        return result

    def query_table(self, table, job_title):
        table = self.con.Table(table)
        response = table.query(
            KeyConditionExpression=Key('job_title').eq(job_title)
        )
        result = response['Items']
        while "LastEvaluatedKey" in response:
            response = table.query(
                KeyConditionExpression=Key('job_title').eq(job_title),
                ExclusiveStartKey=response["LastEvaluatedKey"]
            )
            result.extend(response["Items"])
        return result
