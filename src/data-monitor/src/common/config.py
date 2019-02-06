import os


MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'actuals')
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.environ.get('MONGO_PORT', '27017'))
