from dynamodb_connector import Connector


class DynamoQuery:

    def __init__(self):
        self.con = Connector.get_conn

    def query_table(self, query):
        pass
