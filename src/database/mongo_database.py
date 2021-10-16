import json
import os

import logging
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from src.config import MONGO_CONNECTION_STRING


class MongoDatabase:
    def __init__(self, port=27017):
        self.port = port
        self.mongo_client = self.create_client()

    def create_client(self) -> MongoClient:
        self.mongo_client = MongoClient(MONGO_CONNECTION_STRING)

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

    def import_data(self, data, collection) -> int:
        data = json.loads(data)
        if isinstance(data, list):
            collection.insert_many(data)
        else:
            collection.insert_one(data)
        return os.EX_OK
