from api.v1.models.supported_actuals import SupportedActuals


def get_supported_actuals():
    return [e.name for e in SupportedActuals]


def report_actuals():
    return True
