from flask import request
from flask_restplus import Resource
from werkzeug.exceptions import BadRequest

from api.v1.logic.actuals import report_actuals, get_supported_actuals
from api.v1.models.supported_actuals import SupportedActuals
from api.v1.restplus import api
from api.v1.serializers.actuals import list_of_actuals
from utils.logging import get_logger

log = get_logger(__file__)

ns = api.namespace('actuals',
                   description='Operations related to ingesting data from reporters.')


@ns.route('/')
class ActualsList(Resource):

    @api.expect()
    def get(self):
        """
        Returns list of supported actuals.
        """
        return get_supported_actuals(), 200


@ns.route('/<string:actual_type>')
class Actuals(Resource):

    @api.expect(list_of_actuals)
    def post(self, actual_type: str):
        """
        Ingests data from a specified reporter type.
        """

        if actual_type.upper() not in SupportedActuals.__members__:
            log.debug(f"Called {ns.name} for the not supported actual type: {actual_type}.")
            raise BadRequest(f"Actual type {actual_type} is not supported!")

        data = request.json
        print(data)
        return report_actuals(), 200
