import logging
import pytz
import requests
import time
from datetime import datetime
from random import random

log = logging.getLogger(__file__)


class Reporter(object):

    def __init__(self):
        self._base_url = 'http://127.0.0.1:8000'
        self._datahub_api = 'api/v1/actuals'
        self._type = 'PRICE'
        self._timeout_seconds = 5

    def start(self):
        while True:
            try:
                self._send_actuals()
                time.sleep(self._timeout_seconds)
            except Exception as err:
                log.error('Unhandled error. Shutting down...', exc_info=True)
                raise SystemExit(err)

    def _send_actuals(self):
        payload = self._construct_payload()
        response = requests.post(f'{self._base_url}/{self._datahub_api}/{self._type}', json=payload)
        log.info(f'Send actuals. Response code:{response.status_code}')

    def _construct_payload(self):
        if self._type == 'PRICE':
            return {'value': self._get_value(), 'timestamp': self._get_timestamp_utc()}

    @staticmethod
    def _get_value():
        return random()

    @staticmethod
    def _get_timestamp_utc():
        return datetime.utcnow().astimezone(tz=pytz.utc).isoformat()
