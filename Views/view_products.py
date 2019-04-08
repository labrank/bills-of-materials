from flask import Blueprint, jsonify, request

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
    single_product = next(
        (item for item in elements if item['name'] == name), None)
    resp = jsonify({"product": single_product})
    resp.status_code = 200
    return resp


@products.route('/product', methods=['POST'])
def add_products():
    # to verify if the parts exist to create a new product
    unique_products = set()
    unique_elements = set()
    new_product = request.json
    products = Product.all_products
    parts = Parts.all_parts

    if any(d['product']['name'] ==
           new_product['product']['name'] for d in products):
        return jsonify({"error": "product already exist"})

    # a set of all existing parts
    for item in parts:
        unique_products.add(item['name'])

    # Using recursion to find all parts
    def findPartsOnProduct(d):
        if isinstance(d, dict):
            for value in d.values():
                if isinstance(value, (dict, list)):
                    findPartsOnProduct(value)
                else:
                    unique_elements.add(value)
        elif isinstance(d, list):
            for item in d:
                if isinstance(item, (dict, list)):
                    findPartsOnProduct(item)
                unique_elements.add(item['name'])
        else:
            unique_elements.add(d['name'])

    findPartsOnProduct(new_product)

    # Verify if all the parts exist using sets
    if len(unique_elements.difference(unique_products)) == 0:
        products.append(new_product)
        resp = jsonify({"products": products})
        resp.status_code = 201
    else:
        resp = jsonify({"error": "Some parts does not exist"})
        resp.status_code = 400
    return resp
