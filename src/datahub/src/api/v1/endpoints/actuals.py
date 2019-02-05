from flask import request
from flask_restplus import Resource

from api.v1.logic.actuals import report_actuals
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
        return None, 200


@ns.route('/<string:actual_type>')
class Actuals(Resource):

    @api.expect(list_of_actuals)
    def post(self, actual_type: str):
        """
        Ingests data from a specified reporter type.
        """
        data = request.json
        return report_actuals(actual_type, data), 200
