import flask.scaffold

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api

from app.resources import auth, products


def init_app(app):
    api = Api(app, prefix="/api")
    api.add_resource(auth.Login, "/auth/login")
    api.add_resource(auth.Signup, "/auth/signup")
    api.add_resource(auth.ForgotPassword, "/auth/forgot-password")
    api.add_resource(products.ProductList, "/products")
    api.add_resource(products.ProductGet, "/product/<id>")
