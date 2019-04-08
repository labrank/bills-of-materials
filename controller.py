class Part:
    def __init__(self, id, name, childs):
        self.id = id
        self.name = name
        self.childs = childs


class Parts:
    all_parts = []

    def addPart(single_part):
        elements = Parts.all_parts
        name = single_part['name']
        exist = next((item for item in elements if item['name'] ==
                      name), None)
        if exist:
            return elements
        elements.append(single_part)
        return single_part

    def deletePart(name):
        elements = Parts.all_parts
        elements[:] = [d for d in elements if d['name'] != name]


class Product:
    all_products = []

    def addProduct(single_product):
        elements = Product.all_products

        if any(element['name'] == single_product['name'] for element in elements):
            return elements
        elements.append(single_product)
        return elements

    def deleteProduct(name):
        elements = Product.all_products
        elements[:] = [d for d in elements if d['name'] != name]
