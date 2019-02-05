from flask_restplus import Api
from werkzeug.exceptions import BadRequest

from utils.logging import get_logger

log = get_logger(__file__)

api = Api(version='1.0', title='DataHub API',
          description='This API provides storage functionality of the time series data.')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    return {'message': message}, 500


@api.errorhandler(BadRequest)
def default_error_handler(e):
    message = e.description
    log.debug(message)
    return {'message': message}, 400
