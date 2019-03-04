''' main application and routing logic for birdup '''
from flask import Flask
from .models import DB


def create_app():
    ''' create and configure an instance of the Flask application '''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route("/")
    def root():
        return "welcome to birdup"

    return app
