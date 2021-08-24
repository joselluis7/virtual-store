from datetime import datetime


from app.enums.EStatus import EStatus
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
    created_at = db.Column(db.DateTime, default=datetime.now())

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


class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(30), default=EStatus.CREATED.value, nullable=False)
    item = db.relationship("Item", backref="order", uselist=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"order number: {self.order_number}"


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return (
            f"order number: ${self.order_number} quantity: {self.quantity} user: {self.user.profile.first_name} {self.user.profile.last_name}"
        )
