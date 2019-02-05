import logging
import time

log = logging.getLogger(__file__)


class Reporter(object):

    def __init__(self):
        self._datahub_url = ''
        self.type = ''
        self.timeout_seconds = 30

    def start(self):
        while True:
            try:
                log.info('Reporting actuals')
                time.sleep(self.timeout_seconds)
            except Exception as err:
                log.error('Unhandled error. Shutting down...', exc_info=True)
                raise SystemExit(err)


