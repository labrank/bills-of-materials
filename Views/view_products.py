from flask import jsonify, request, Blueprint

from controller import Part, Parts, Product

products = Blueprint('products', __name__)

@products.route('/products', methods=['GET'])
def get_products():
    resp = jsonify({"name": Product.all_products})
    resp.status_code = 200
    return resp

@products.route('/product/<string:name>', methods=['GET'])
def add_part(name):
    elements = Parts.all_parts
    single_product = Part(len(elements) +1, part['name'], part['childs'])
    Parts.addPart(single_part.__dict__)
    resp = jsonify({"parts": Parts.all_parts})
    resp.status_code = 201
    return resp

@products.route('/parts', methods=['POST'])
def add_parts():
    parts = request.json['parts']
    last_id = len(Parts.all_parts) + 1
    for part in parts:
        single_part = Part(last_id, part['name'], part['childs'])
        Parts.addPart(part)
    resp = jsonify({"parts": Parts.all_parts})
    resp.status_code = 201
    return resp

@products.route('/part/<string:name>', methods=['POST'])
def add_assemblies(name):
    elements = Parts.all_parts
    parts = request.json['childs']
    index = next((index for (index, d) in enumerate(elements) if d["name"] == name), None)

    if index:
        elements[index]["childs"].extend(parts)
        resp = jsonify({"values":elements[index]})
    else:
        resp = jsonify({"error":"no element"})
    resp.status_code = 200
    return resp

@products.route('/part/<string:name>', methods=['DELETE'])
def delete_parts(name):
    try:
        resp = jsonify(Parts.deletePart(name))
        resp.status_code = 204
    except:
        resp = jsonify('Element does not exist')
        resp.status_code = 404
    return resp

@products.route('/assemblies', methods=['GET'])
def get_assemblies():
    elements = Parts.all_parts
    are_assemblies = [e for e in elements if len(e.get('childs')) > 0]

    if are_assemblies:
        resp = jsonify({"assemblies":are_assemblies})
        resp.status_code = 200
    else:
        resp = jsonify({"error":"no assemblies"})
        resp.status_code = 404
    return resp


@products.route('/components', methods=['GET'])
def get_components():
    elements = Parts.all_parts
    are_assemblies = [e for e in elements if len(e.get('childs')) == 0]

    if are_assemblies:
        resp = jsonify({"components":are_assemblies})
        resp.status_code = 200
    else:
        resp = jsonify({"error":"no assemblies"})
        resp.status_code = 404
    return resp
