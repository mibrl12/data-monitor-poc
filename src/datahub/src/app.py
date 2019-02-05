from flask import Flask, Blueprint, redirect


from api.v1.restplus import api
from api.v1.endpoints.actuals import ns as intersect_namespace


app = Flask(__name__)


def setup_app(flask_app):
    blueprint_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
    api.init_app(blueprint_v1)
    api.add_namespace(intersect_namespace)
    flask_app.register_blueprint(blueprint_v1)


setup_app(app)


@app.route("/")
def root():
    return redirect("/api/v1", code=302)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
