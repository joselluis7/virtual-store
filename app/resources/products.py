

from flask_restful import Resource, marshal_with, marshal

from app.extension import db
from app.models import Category, Product
from app.response_template import products_fields



class ProductList(Resource):
    @marshal_with(products_fields, envelope="products")
    def get(self):
        products = Product.query.all()
        return  products 

class ProductGet(Resource):
    def get(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            return {"error":"product does not exists"}, 400
        return marshal(product, products_fields, "product")


