from pymongo import MongoClient

from common import config


db_client = MongoClient(host=config.MONGO_HOST, port=config.MONGO_PORT)
db = db_client[config.MONGO_DBNAME]
