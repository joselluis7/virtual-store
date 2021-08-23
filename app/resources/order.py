import logging
from datetime import datetime

from app.extension import db
from app.models import Item, Order, Product
from app.response_template import order_fields
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_migrate import current
from flask_restful import Resource, marshal, reqparse


class Create(Resource):

    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument(
            "product_id", type=int, required=True, help="required field"
        )
        parser.add_argument("quantity", type=int, required=True, help="required field")
        args = parser.parse_args()

        product = Product.query.get(args.product_id)
        print(f"{product.id} EPERA ")
        if not product :
            return {"error": "product does not exists"}, 400

        if args.quantity > product.quantity:
            return {"error": "invalid quantity"}, 400

        try:
            order = Order()
            #remove 4 digits from miliseconds
            order.order_number = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-4]
            db.session.add(order)
            db.session.commit()

            item = Item()
            item.order_id = order.id
            item.prduct_id = product.id
            item.user_id = current_user['id']
            item.quantity = args.quantity
            item.price = product.price * item.quantity 
            db.session.add(item)
            db.session.commit()
            marshal(order, order_fields, "order")
        except Exception as e :
            logging.critical(str(e))
            db.session.rollback()
            return {"error": "unable to create order"}, 500

        return "teste"

class Pay(Resource):
    pass


class Notification(Resource):
    pass
