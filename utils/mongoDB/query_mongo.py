import sys
from .mongo_connector import Connector
import logging

database_name = "jobs_data"
mongo = Connector(database_name)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


class MongoQuery:

    def __init__(self):
        self.client = mongo.get_client

    def list_tables(self):
        result = list()
        for record in list(self.client.tables.all()):
            result.append(record.name)
        return result

    def get_all_records(self, table_name):
        result = list()
        collection = self.client[database_name][table_name]
        try:
            response = collection.find({}, {'_id': 0})
            for i in response:
                result.append(i)
        except Exception as e:
            logger.exception(e)
            return {"data": f"query failed due to : {e}"}
        return result

    def query_table(self, table_name, job_title):
        result = list()
        collection = self.client[database_name][table_name]
        try:
            response = collection.find({'job_title': {'$regex': job_title, '$options': "$i"}}, {'_id': 0})
            for i in response:
                result.append(i)
        except Exception as e:
            logger.exception(e)
            return {"data": f"query failed due to : {e}"}
        return result
