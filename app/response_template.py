from os import pathconf
from flask_restful import fields


categories_fields = {"name": fields.String, "slug": fields.String}

products_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "slug": fields.String,
    "price": fields.Float,
    "quantity": fields.Integer,
    "description": fields.String,
    "categories": fields.Nested(categories_fields),
}
item_fields = {"quantity": fields.Integer, "price": fields.Float}

order_fields = {
    "id": fields.Integer,
    "order_number": fields.String,
    "item": fields.Nested(item_fields),
    "status": fields.String,
}
user_orders_fields = {
    "order": fields.Nested(order_fields),
    "product": fields.Nested(products_fields)
}
profile_fields = {
    "first_name": fields.String,
    "last_name": fields.String,
    "document_id": fields.String,
    "phone": fields.String
    }