```python
import unittest
from src import partnerships

class TestPartnerships(unittest.TestCase):

    def setUp(self):
        self.partnerships = partnerships.Partnerships()

    def test_create_partnership(self):
        result = self.partnerships.create_partnership('Company A', 'Company B')
        self.assertEqual(result, 'Partnership created between Company A and Company B')

    def test_remove_partnership(self):
        self.partnerships.create_partnership('Company A', 'Company B')
        result = self.partnerships.remove_partnership('Company A', 'Company B')
        self.assertEqual(result, 'Partnership between Company A and Company B removed')

    def test_get_partners(self):
        self.partnerships.create_partnership('Company A', 'Company B')
        result = self.partnerships.get_partners('Company A')
        self.assertEqual(result, ['Company B'])

    def test_get_all_partnerships(self):
        self.partnerships.create_partnership('Company A', 'Company B')
        self.partnerships.create_partnership('Company A', 'Company C')
        result = self.partnerships.get_all_partnerships()
        self.assertEqual(result, [('Company A', 'Company B'), ('Company A', 'Company C')])

if __name__ == '__main__':
    unittest.main()
```