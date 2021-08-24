import logging


from flask_restful import Resource, marshal_with, reqparse


from app.response_template import categories_fields
from app.models import Category
from app.extension import db


class Create(Resource):

    def post(self):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument("name", required=True, help="required field")
        parser.add_argument("slug", required=True, help="required field")
        args = parser.parse_args()
        print("FFFF: ", args.name)

        category = Category.query.filter_by(slug=args.slug).first()
        print(category)
        if not category:
            category = Category(name=args.name, slug=args.slug)
            db.session.add(category)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                logging.critical(str(e))
                return {"error": "something went wrong"}, 500

            logging.info(f"Category {args.name} created successfully")
            return {"message": "category added successfully "}, 200
        return {"mesage": "category already exists"}, 201


class ListCategory(Resource):

    @marshal_with(categories_fields, envelope="categories")
    def get(self):
        category = Category.query.all()
        return category
