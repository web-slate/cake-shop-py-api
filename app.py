from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

# Init App.
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite://' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;

# Init DB.
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

# Product Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  image = db.Column(db.String(250))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)
  color = db.Column(db.String(50))
  currency = db.Column(db.String(50))

  def __init__(self, name, image, price, color, currency):
    self.name = name
    self.image = image
    self.price = price
    self.color = color
    self.currency = currency

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ( 'id', 'name', 'image', 'price', 'qty', 'color', 'currency' )

# Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many = True)

# Create a Product
@app.route('/product', methods=['post'])
def add_new_product():
  name = request.json['name']
  price = request.json['price']
  qty = request.json['qty']
  color = request.json['color']
  currency = request.json['currency']

@app.route('/')
def index():
    return "Welcome to Cake Shop APIs"

@app.route('/product-list', methods=['GET'])
def getProductList():
    return jsonify({
        'products': [
            {
                'name': 'Chock Birthday Cake',
                'image': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2955&q=80',
                'price': 250,
                'color': 'Brown',
                'currency': 'INR',
            },
            {
                'name': 'Cup Cake',
                'image': 'https://images.unsplash.com/photo-1550617931-e17a7b70dce2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
                'price': 16,
                'color': 'Black',
                'currency': 'INR',
            },
            {
                'name': 'Fruit Cake',
                'image': 'https://images.unsplash.com/photo-1514056052883-d017fddd0426?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
                'price': 25,
                'currency': 'INR',
            },
            {
                'name': '3 Step Flow Cake',
                'image': 'https://images.unsplash.com/photo-1561702856-b4ec96854ed8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
                'price': 700,
                'currency': 'INR',
            },
            {
                'name': '4 Step Flow Cake',
                'image': 'https://images.unsplash.com/photo-1535254973040-607b474cb50d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
                'price': 907,
                'currency': 'INR',
            }
        ]
    })

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
