```python
import unittest
from src import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = main.create_app()

    def test_app_creation(self):
        self.assertIsNotNone(self.app)

    def test_event_management(self):
        response = self.app.test_client().get('/event_management')
        self.assertEqual(response.status_code, 200)

    def test_recommendation_system(self):
        response = self.app.test_client().get('/recommendation_system')
        self.assertEqual(response.status_code, 200)

    def test_virtual_networking(self):
        response = self.app.test_client().get('/virtual_networking')
        self.assertEqual(response.status_code, 200)

    def test_analytics(self):
        response = self.app.test_client().get('/analytics')
        self.assertEqual(response.status_code, 200)

    def test_operations(self):
        response = self.app.test_client().get('/operations')
        self.assertEqual(response.status_code, 200)

    def test_automation_tools(self):
        response = self.app.test_client().get('/automation_tools')
        self.assertEqual(response.status_code, 200)

    def test_scalability(self):
        response = self.app.test_client().get('/scalability')
        self.assertEqual(response.status_code, 200)

    def test_customer_support(self):
        response = self.app.test_client().get('/customer_support')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```