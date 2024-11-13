from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from config import Config

# Initialize Flask app and configurations
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
swagger = Swagger(app)

# Define database model
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Example endpoint with Swagger documentation
@app.route('/products', methods=['GET'])
def get_products():
    """
    Get a list of products
    ---
    responses:
      200:
        description: A list of products
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: The product ID
              name:
                type: string
                description: The product name
              price:
                type: number
                description: The product price
    """
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products])

# Run app
if __name__ == '__main__':
    app.run(debug=True)
