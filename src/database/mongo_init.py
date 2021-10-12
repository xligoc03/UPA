import os

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class MongoDatabase:
    def __init__(self, port=27017):
        self.port = port
        self.mongo_client = None

    def create_client(self) -> MongoClient:
        self.mongo_client = MongoClient('localhost', self.port)
        return self.mongo_client

    def check_connection(self):
        try:
            self.mongo_client.admin.command('ping')
        except ConnectionFailure:
            print("Server not available")

        return os.EX_OK

    def close_client(self):
        self.mongo_client.close()

    def print_info(self):
        print(self.mongo_client)
