import os

import logging
import json
import xmltodict
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from src.config import DB_HOST, DB_PSWD, DB_USER


class MongoDatabase:
    def __init__(self, port=27017):
        self.port = port
        self.mongo_client = self.create_client()

    def create_client(self) -> MongoClient:
        self.mongo_client = MongoClient('mongodb://%s:%s@%s' % (DB_USER, DB_PSWD, DB_HOST))
        return self.mongo_client

    def create_db(self, db_name):
        return self.mongo_client[db_name]

    def check_connection(self, client) -> int:
        if client is None:
            client = self.create_client()

        try:
            client.admin.command('ping')
        except ConnectionFailure:
            logging.error("Server not available")

        return os.EX_OK

    def close_client(self):
        self.mongo_client.close()

    def print_info(self):
        if self.mongo_client is None:
            logging.warning("Database client is not connected")
        else:
            print(self.mongo_client)

    def import_data(self, xml, db_name, collection) -> int:
        with open(xml, 'r') as file:
            data = file.read()
        # convert XML to json string and than to dict
        json_data = json.loads(json.dumps(xmltodict.parse(data)))["ExportDat"]["PravniSubjekt"]

        database = self.create_db(db_name)
        collection = database[collection]

        if isinstance(json_data, list):
            collection.insert_many(json_data)
        else:
            collection.insert_one(json_data)
        return 0
