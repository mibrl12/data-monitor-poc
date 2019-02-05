from flask import Flask, Blueprint, redirect

from api.v1.restplus import api
from api.v1.endpoints.actuals import ns as actuals_namespace
from common import config

app = Flask(__name__)


def setup_app(flask_app):

    from common.db import mongo
    app.config.from_object(config)
    mongo.init_app(app, 'mongodb://localhost:27017/actuals')

    blueprint_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
    api.init_app(blueprint_v1)
    api.add_namespace(actuals_namespace)
    flask_app.register_blueprint(blueprint_v1)


setup_app(app)


@app.route("/")
def root():
    return redirect("/api/v1", code=302)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
