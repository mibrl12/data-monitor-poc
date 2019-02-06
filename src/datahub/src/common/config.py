import os


MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'actuals')
MONGO_URL = os.environ.get('MONGO_URL', 'mongodb://localhost:27017')
