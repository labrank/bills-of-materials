from flask import jsonify, request, Blueprint

from controller import Part, Parts, Product

products = Blueprint('products', __name__)

@products.route('/products', methods=['GET'])
def get_products():
    resp = jsonify({"name": Product.all_products})
    resp.status_code = 200
    return resp

@products.route('/product/<string:name>', methods=['GET'])
def get_product(name):
    elements = Product.all_products
    single_product = next((item for item in elements if item['name'] == name), None)
    resp = jsonify({"product": single_product})
    resp.status_code = 200
    return resp

@products.route('/product', methods=['POST'])
def add_products():
    products = Product.all_products
    parts = Parts.all_parts
    new_products = request.json
    last_id = len(Parts.all_parts) + 1
    for part in parts:
        single_part = Part(last_id, part['name'], part['childs'])
        Parts.addPart(part)
    resp = jsonify({"parts": Parts.all_parts})
    resp.status_code = 201
    return resp
