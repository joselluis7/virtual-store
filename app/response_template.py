from flask_restful import fields


products_fields = {
    "id" : fields.Integer,
    "name": fields.String,
    "slug": fields.String, 
    "price": fields.Float,
    "quantity":fields.Integer,
    "description": fields.String
}