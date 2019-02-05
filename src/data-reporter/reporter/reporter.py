import logging
import time

import requests

log = logging.getLogger(__file__)


class Reporter(object):

    def __init__(self):
        self._base_url = 'http://127.0.0.1:8000'
        self._datahub_api = 'api/v1/actuals'
        self._type = 'PRICE'
        self._timeout_seconds = 30

    def start(self):
        while True:
            try:
                self._send_actuals()
                time.sleep(self._timeout_seconds)
            except Exception as err:
                log.error('Unhandled error. Shutting down...', exc_info=True)
                raise SystemExit(err)

    def _send_actuals(self):
        response = requests.post(f'{self._base_url}/{self._datahub_api}/{self._type}', json={"key": "value"})
        log.info(f'Send actuals. Response code:{response.status_code}')
