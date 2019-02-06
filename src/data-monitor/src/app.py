import logging

import prometheus_client

from common import config
from monitor.datamonitor import PriceDataMonitor

log = logging.getLogger(__file__)


def main():
    log.info('Starting data-monitor')

    prometheus_client.start_http_server(config.MONITORING_PORT)

    from common.db import db
    datamonitor = PriceDataMonitor(db=db)
    datamonitor.start()


if __name__ == '__main__':
    main()

