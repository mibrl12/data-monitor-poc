from datetime import datetime

import pytz
from werkzeug.exceptions import BadRequest

from api.v1.models.supported_actuals import SupportedActuals
from api.v1.serializers.actuals import actual
from common.db import mongo


def get_supported_actuals():
    return [e.name for e in SupportedActuals]


def report_actuals(actual_type: str, data: actual):
    actuals = data.get('actuals')

    processing_time = _get_timestamp_utc()
    for actual in actuals:
        actual['processed_timestamp'] = processing_time

    if actual_type.upper() == SupportedActuals.PRICE.name:
        mongo.db.prices.insert(actuals)
    elif actual_type.upper() == SupportedActuals.CONSUMPTION.name:
        mongo.db.consumption.insert(actuals)
    elif actual_type.upper() == SupportedActuals.PRODUCTION.name:
        mongo.db.prodution.insert(actuals)
    else:
        raise BadRequest(f"Actual type {actual_type} is not supported!")


def _get_timestamp_utc():
    return datetime.utcnow().astimezone(tz=pytz.utc).isoformat()
