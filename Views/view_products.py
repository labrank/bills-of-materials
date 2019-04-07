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
    unique_products = set()
    unique_elements = set()
    products = Product.all_products
    parts = Parts.all_parts
    new_products = request.json#['product']#['parts']
    for item in parts:
        unique_products.add(item['name'])

    print('-'*10)
    def childToSet(d):
        if isinstance(d, dict):
            for key, value in d.items():
                if isinstance(value, (dict, list)):
                    childToSet(value)
                else:
                    unique_elements.add(value)
        elif isinstance(d, list):
            for item in d:
                if isinstance(item, (dict, list)):
                    childToSet(item)
                unique_elements.add(item['name'])
        else:
            unique_elements.add(d['name'])

    childToSet(new_products)
    print('lista final:')
    print(unique_elements)
    products.append(new_products)


    return jsonify({"products": products})
