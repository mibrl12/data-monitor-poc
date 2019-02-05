import logging

from common import config
from reporter.reporter import Reporter

log = logging.getLogger(__file__)


def main():
    log.info('Starting reporter')

    reporter = Reporter(reporter_type=config.REPORTER_TYPE,
                        datahub_base_url=config.DATAHUB_BASE_URL,
                        actuals_api=config.DATAHUB_API,
                        delay_seconds=config.DELAY_SECONDS)
    reporter.start()


if __name__ == '__main__':
    main()

