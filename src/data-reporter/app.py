import logging

from reporter.reporter import Reporter

log = logging.getLogger(__file__)


def main():
    log.info('Starting reporter')

    reporter = Reporter()
    reporter.start()


if __name__ == '__main__':
    main()

