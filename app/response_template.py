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
item_fields = {
    "quantity": fields.Integer,
    "price": fields.Float
}

order_fields = {
    "reference_id": fields.String,
    "items": fields.Nested(item_fields),
    "status": fields.String

}