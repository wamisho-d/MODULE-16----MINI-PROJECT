import unittest
from app import app, db, Product

class APITestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_products(self):
        # Add a test product to the database
        product = Product(name="Test Product", price=19.99)
        with app.app_context():
            db.session.add(product)
            db.session.commit()

        # Test the /products endpoint
        response = self.client.get('/products')
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertEqual(data[0]["name"], "Test Product")
        self.assertEqual(data[0]["price"], 19.99)

if __name__ == '__main__':
    unittest.main()
