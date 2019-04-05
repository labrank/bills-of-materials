class Parts:
    all_parts = {1:"part1"}

    def addPart(name):
        elements = Parts.all_parts
        if(name in elements.values()):
            return elements
        elements[len(elements) + 1] = name
        return elements

    def deletePart(name):
        elements = Parts.all_parts
        for key, value in elements.items():
            if value == name:
                del elements[key]
                return 'ok'
            else:
                raise Exception('Element does not exist')
