```python
import unittest
from src import updates

class TestUpdates(unittest.TestCase):

    def setUp(self):
        self.updates = updates.Updates()
        self.eventData = {
            "event_id": "123",
            "event_name": "Virtual Concert",
            "event_date": "2022-12-31",
            "event_time": "18:00",
            "event_description": "A virtual concert featuring popular artists."
        }
        self.userData = {
            "user_id": "456",
            "user_name": "John Doe",
            "user_email": "johndoe@example.com"
        }

    def test_send_update(self):
        result = self.updates.send_update(self.userData, self.eventData, "eventUpdate")
        self.assertEqual(result, "Update sent successfully")

    def test_receive_update(self):
        result = self.updates.receive_update(self.userData, "eventUpdate")
        self.assertEqual(result, "Update received successfully")

if __name__ == '__main__':
    unittest.main()
```