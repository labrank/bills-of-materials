from flask import jsonify, request, Blueprint

from controller import Part, Parts

parts = Blueprint('parts', __name__)


@parts.route('/parts', methods=['GET'])
def get_parts():
    resp = jsonify({"parts": Parts.all_parts})
    resp.status_code = 200
    return resp


@parts.route('/part', methods=['POST'])
def add_part():
    part = request.json
    elements = Parts.all_parts
    single_part = Part(len(elements) + 1, part['name'], part['childs'])
    Parts.addPart(single_part.__dict__)
    resp = jsonify({"parts": Parts.all_parts})
    resp.status_code = 201
    return resp


@parts.route('/parts', methods=['POST'])
def add_parts():
    parts = request.json['parts']
    last_id = len(Parts.all_parts)
    for part in parts:
        single_part = Part(last_id, part['name'], part['childs'])
        Parts.addPart(single_part.__dict__)
        last_id += 1
    resp = jsonify({"parts": Parts.all_parts})
    resp.status_code = 201
    return resp


@parts.route('/part/<string:name>', methods=['POST'])
def add_assemblies(name):
    elements = Parts.all_parts
    parts = request.json['childs']
    index = next((index for (index, d) in enumerate(
        elements) if d["name"] == name), None)

    if index:
        elements[index]["childs"].extend(parts)
        resp = jsonify({"values": elements[index]})
    else:
        resp = jsonify({"error": "no element"})
    resp.status_code = 200
    return resp


@parts.route('/part/<string:name>', methods=['DELETE'])
def delete_parts(name):
    try:
        resp = jsonify(Parts.deletePart(name))
        resp.status_code = 204
    except:
        resp = jsonify('Element does not exist')
        resp.status_code = 404
    return resp
