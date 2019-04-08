import unittest

from api import app
from controller import Part, Parts, Product


class TestControllers(unittest.TestCase):

    def setUp(self):
        self.id = 1
        self.name = 'test part'
        self.childs = []
        self.part = Part(self.id, self.name, self.childs)

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_isAddingPart(self):
        Parts.addPart(self.part.__dict__)
        size = len(Parts.all_parts)
        self.assertEqual(size, 1)

    def test_isDeletingPart(self):
        Parts.deletePart(self.name)
        size = len(Parts.all_parts)
        self.assertEqual(size, 0)

    def test_isAddingProduct(self):
        parts = Parts.addPart(self.part.__dict__)
        Product.addProduct(parts)
        size = len(Product.all_products)
        self.assertEqual(size, 1)

    @unittest.skip("Delete will be implemented furter")
    def test_isDeletingProduct(self):
        Product.deleteProduct(self.name)
        size = len(Product.all_products)
        self.assertEqual(size, 0)


if __name__ == '__main__':
    unittest.main()
