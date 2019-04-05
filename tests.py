from app import app

import unittest


class CheckEndPoints(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_parts(self):
        tester = app.get_parts(self)
        response = tester.get('/parts', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_assemblies(self):
        tester = app.get_assemblies(self)
        response = tester.get('/assemblies', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_top_assemblies(self):
        tester = app.get_top_assemblies(self)
        response = tester.get('/top-assemblies', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_subassemblies(self):
        tester = app.test_subassemblies(self)
        response = tester.get('/subassemblies', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
