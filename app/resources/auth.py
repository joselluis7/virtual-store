import logging
from base64 import b64decode
from datetime import timedelta

from app.extension import db
from app.models import User
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash, generate_password_hash


class Login(Resource):

    def get(self):
        if not request.headers.get("Authorization"):
            return {"error": "authorization not found"}, 400

        basic, code = request.headers["Authorization"].split(" ")
        print(code)
        if not basic.lower() == "basic":
            return {"error": "bad authorization"}, 400

        email, password = b64decode(code).decode().split(":")
        print("email", email)
        print("password", password)
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return {
                "error": "authentication fails! user or password are incorrect"
            }, 400

        token = create_access_token({"id": user.id}, expires_delta=timedelta(minutes=5))

        return {"encoded_token": token}


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
            user = User(
                email=args.email, password=generate_password_hash(args.password)
            )
            db.session.add(user)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                logging.critical(str(e))
                return jsonify({"error": "something went wrong"}), 500
            return jsonify({"message": "user added successfully"})
        return jsonify({"error": "user already exists"})
