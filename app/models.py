from enum import unique

from sqlalchemy.orm import backref
from app.extension import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return self.email


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), nullable=False, unique=True, index=True)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.LargeBinary, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey("categories.id"))

    def __repr__(self):
        return self.name

class Category(db.Model):

    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(150), nullable=False, unique=True, index=True)
    products = db.relationship("Product", backref="categories", uselist=True)

    def __repr__(self):
        return self.name

    