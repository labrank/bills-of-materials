class Part:
    def __init__(self, id, name, childs):
        self.id = id
        self.name = name
        self.childs = childs


class Parts:
    all_parts = []

    def addPart(Part):
        elements = Parts.all_parts
        if any(element['name'] == Part['name'] for element in elements):
            return elements
        elements.append(Part)
        return elements

    def deletePart(name):
        elements = Parts.all_parts
        elements[:] = [d for d in elements if d.get('name') != name]
