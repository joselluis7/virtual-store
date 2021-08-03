import logging

from flask import jsonify
from flask_restful import Resource, reqparse

from app.extension import db
from app.models import User


class Login(Resource):

    def get(self):
        return {"pagina": "Login"}


class Signup(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", required=True, help="email field is required")
        parser.add_argument(
            "password", required=True, help="password field is required"
        )
        args = parser.parse_args()

        user = User.query.filter_by(email=args.email).first()
        if not user:
            user = User(email=args.email, password=args.password)
            db.session.add(user)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                logging.critical(str(e))
                return jsonify({"error": "something went wrong"}), 500
            return jsonify({"message": "user added successfully"})
        return jsonify({"error": "user already exists"})
