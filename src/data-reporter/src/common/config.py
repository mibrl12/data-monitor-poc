import os

REPORTER_TYPE = os.environ.get('REPORTER_TYPE', 'PRICE')
DATAHUB_BASE_URL = os.environ.get('DATAHUB_BASE_URL', 'http://127.0.0.1:8000')
DATAHUB_API = os.environ.get('DATAHUB_API', 'api/v1/actuals')
DELAY_SECONDS = int(os.environ.get('DELAY_SECONDS', '5'))
