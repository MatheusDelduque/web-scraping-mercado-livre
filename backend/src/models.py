from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    name = db.Column(db.String, nullable=False, primary_key=True)
    brand = db.Column(db.String, nullable=False)
    old_price = db.Column(db.Float, nullable=False)
    new_price = db.Column(db.Float, nullable=False)
    reviews_rating_number = db.Column(db.Float, nullable=False)
    reviews_amount = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'name': self.name,
            'brand': self.brand,
            'old_price': self.old_price,
            'new_price': self.new_price,
            'reviews_rating_number': self.reviews_rating_number,
            'reviews_amount': self.reviews_amount
        }
