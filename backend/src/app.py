from flask import Flask, jsonify
from config import Config
from models import db, Product

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_request
def before_request_func():
    if not hasattr(app, 'db_initialized'):
        with app.app_context():
            db.create_all()
        app.db_initialized = True

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
