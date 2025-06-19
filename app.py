from flask import Flask
from flask_smorest import Api
from resources.notes import blp as NotesBLuePrint
from db import db

app = Flask(__name__)

def create_app():
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Simple Notes REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)



    api = Api(app)

    api.register_blueprint(NotesBLuePrint)

    return app

if __name__== "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)