import os
import pymongo


class Connector:
    def __init__(self, db):
        self._mongo_pass = os.environ.get("mongo_password")
        self._mongo_user = os.environ.get("mongo_user")
        self._mongo_cluster = os.environ.get("mongo_cluster")
        self._mongo_db = db
        self._uri = f"mongodb+srv://{self._mongo_user}:{self._mongo_pass}" \
                    f"@{self._mongo_cluster}.mongodb.net/{self._mongo_db}?retryWrites=true&w=majority"
        self.client = None

    @property
    def get_client(self):
        if self.client:
            return self.client
        else:
            client = pymongo.MongoClient(self._uri)
            return client

