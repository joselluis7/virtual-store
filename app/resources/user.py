from flask_restful import Resource, marshal
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models import User
from app.response_template import user_orders_fields

class Orders(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.get(current_user['id'])
        return marshal(user.item, user_orders_fields)
