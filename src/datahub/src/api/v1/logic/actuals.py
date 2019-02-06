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

    if actual_type.upper() not in SupportedActuals.__members__:
        raise BadRequest(f"Actual type {actual_type} is not supported!")

    mongo.db[actual_type.lower()].insert(actuals)


def _get_timestamp_utc():
    return datetime.utcnow().astimezone(tz=pytz.utc).isoformat()
