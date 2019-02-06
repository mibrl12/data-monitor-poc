import logging

from monitor.datamonitor import PriceDataMonitor

log = logging.getLogger(__file__)


def main():
    log.info('Starting data-monitor')

    from common.db import db
    datamonitor = PriceDataMonitor(db=db)
    datamonitor.start()


if __name__ == '__main__':
    main()

