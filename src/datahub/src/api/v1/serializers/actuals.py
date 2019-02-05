from flask_restplus import fields
from api.v1.restplus import api


actual = api.model('Actual', {
})

price = api.inherit('Price', actual, {
    'value': fields.Float(required=True),
    'timestamp': fields.DateTime(required=True)
})

list_of_actuals = api.model('A list of actuals', {
    'actuals': fields.List(fields.Nested(actual))
})
