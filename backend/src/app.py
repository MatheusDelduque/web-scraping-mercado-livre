from flask import Flask, jsonify
from config import Config
from models import db, Product
from sqlalchemy import func
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

db.init_app(app)


@app.before_request
def before_request_func():
    if not hasattr(app, 'db_initialized'):
        with app.app_context():
            db.create_all()
        app.db_initialized = True


@app.route('/brand_count', methods=['GET'])
def get_brand_count():
    brand_counts = db.session.query(
        Product.brand,
        func.count(Product.brand).label('count')
    ).filter(Product.brand != "").group_by(Product.brand).all()

    return jsonify({brand: count for brand, count in brand_counts})

@app.route('/average_price', methods=['GET'])
def get_average_price_of_each_brand():
    brand_prices = db.session.query(
        Product.brand,
        func.avg(Product.new_price).label('average_price')
    ).filter(Product.brand != "").group_by(Product.brand).all()
   
    return jsonify({brand: price for brand, price in brand_prices})

@app.route('/brand_average_rating_number_reviews', methods=['GET'])
def get_review_count():
    brand_counts = db.session.query(
        Product.brand,
        func.avg(Product.reviews_rating_number).label('average_rating_number_reviews')
    ).filter(Product.brand != "").group_by(Product.brand).all()

    return jsonify({brand: reviews_rating_number for brand, reviews_rating_number in brand_counts})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
