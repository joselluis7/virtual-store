from flask import Flask


from app import extension
from app import routes


def create_app():
    app = Flask(__name__)
    extension.init_app(app)
    routes.init_app(app)
    return app
