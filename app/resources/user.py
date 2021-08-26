import logging

from flask_restful import Resource, marshal, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models import User, Profile
from app.extension import db
from app.response_template import user_orders_fields, profile_fields


class ProfileUpdate(Resource):
    @jwt_required
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("first_name", required=True, help="mandatory field")
        parser.add_argument("last_name", required=True, help="mandatory field")
        parser.add_argument("document", required=True, help="mandatory field")
        parser.add_argument("phone", required=True, help="mandatory field")
        args = parser.parse_args(strict=True)

        current_user = get_jwt_identity()

        user = User.query.get(current_user["id"])

        if not user.profile:
            user.profile = Profile()
        
        user.profile.first_name = args.first_name
        user.profile.last_name = args.last_name
        user.profile.document_id = args.document
        user.profile.phone = args.phone

        try:
            db.session.commit()
            
        except Exception as e:
            logging.critical(f"{str(e)}")
            db.session.rollback()
            return {"error":"unable to update profile"}

        return marshal(user.profile, profile_fields, "profile")


        

class Orders(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.get(current_user['id'])
        return marshal(user.item, user_orders_fields)
