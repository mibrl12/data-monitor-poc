import logging
import pytz
import requests
import time
from datetime import datetime
from random import random

from models.supported_actuals import SupportedActuals

log = logging.getLogger(__file__)


class Reporter(object):

    def __init__(self, reporter_type: str, datahub_base_url: str,
                 actuals_api: str, delay_seconds: int):
        self._type = reporter_type
        self._datahub_base_url = datahub_base_url
        self._actuals_api = actuals_api
        self._delay_seconds = delay_seconds

    def start(self):
        while True:
            try:
                self._send_actuals()
                time.sleep(self._delay_seconds)
            except Exception as err:
                log.error('Unhandled error. Shutting down...', exc_info=True)
                raise SystemExit(err)

    def _send_actuals(self):
        payload = self._construct_payload()
        response = requests.post(f'{self._datahub_base_url}/{self._actuals_api}/{self._type}', json=payload)
        log.info(f'Send actuals. Response code:{response.status_code}')

    def _construct_payload(self):
        if self._type == SupportedActuals.PRICE.name:
            return {'actuals': [{'name': self._get_commodity_name(),
                                 'value': self._get_value(),
                                 'timestamp': self._get_timestamp_utc()}]}

    @staticmethod
    def _get_commodity_name():
        return 'MWh'

    @staticmethod
    def _get_value():
        return random()

    @staticmethod
    def _get_timestamp_utc():
        return datetime.utcnow().astimezone(tz=pytz.utc).isoformat()
