import logging

from flask import request
from flask_restplus import Resource

from api.v1.logic.actuals import report_actuals
from api.v1.restplus import api
from api.v1.serializers.actuals import list_of_actuals

log = logging.getLogger(__name__)

ns = api.namespace('actuals',
                   description='Operations related to ingesting data from reporters.')


@ns.route('/<string:actual_type>')
class Actuals(Resource):

    @api.expect(list_of_actuals)
    def post(self, actual_type: str):
        """
        Ingests data from a specified reporter type.
        """
        data = request.json
        print(data)
        return report_actuals(), 200
