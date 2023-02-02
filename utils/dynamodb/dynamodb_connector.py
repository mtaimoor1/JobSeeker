import boto3
import os


class Connector:
    def __init__(self):
        self.con = None

    @property
    def get_conn(self):
        if self.con:
            return self.con
        else:
            return boto3.client("dynamodb", aws_access_key_id=os.environ.get("aws-access-key"),
                                aws_secret_access_key=os.environ.get("aws-secret-key"))
