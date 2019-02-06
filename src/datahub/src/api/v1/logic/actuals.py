from werkzeug.exceptions import BadRequest

from api.v1.models.supported_actuals import SupportedActuals
from api.v1.serializers.actuals import actual
from common.db import mongo


def get_supported_actuals():
    return [e.name for e in SupportedActuals]


def report_actuals(actual_type: str, data: actual):
    actuals = data.get('actuals')
    if actual_type.upper() == SupportedActuals.PRICE.name:
        mongo.db.prices.insert(actuals)
    elif actual_type.upper() == SupportedActuals.CONSUMPTION.name:
        mongo.db.consumption.insert(actuals)
    elif actual_type.upper() == SupportedActuals.PRODUCTION.name:
        mongo.db.prodution.insert(actuals)
    else:
        raise BadRequest(f"Actual type {actual_type} is not supported!")
