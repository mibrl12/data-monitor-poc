import logging
import os
import sys

loggers = {}
handlers = []


def get_logger(name):
    global loggers
    logger = loggers.get(name)
    if logger:
        return logger

    logger = logging.getLogger(name)
    logger.setLevel(os.getenv('LOG_LEVEL', 'DEBUG'))
    handler = logging.StreamHandler(sys.stdout)
    handlers.append(handler)

    logger.propagate = False
    logger.addHandler(handler)
    loggers[name] = logger
    return logger
