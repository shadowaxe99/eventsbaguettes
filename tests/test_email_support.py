```python
import unittest
from src import email_support

class TestEmailSupport(unittest.TestCase):

    def setUp(self):
        self.email_support = email_support.EmailSupport()

    def test_send_email(self):
        result = self.email_support.send_email("test@example.com", "Test Subject", "Test Body")
        self.assertTrue(result)

    def test_send_bulk_email(self):
        emails = ["test1@example.com", "test2@example.com", "test3@example.com"]
        result = self.email_support.send_bulk_email(emails, "Test Subject", "Test Body")
        self.assertTrue(result)

    def test_send_event_update(self):
        result = self.email_support.send_event_update("test@example.com", "Test Event", "Test Update")
        self.assertTrue(result)

    def test_send_registration_confirmation(self):
        result = self.email_support.send_registration_confirmation("test@example.com", "Test Event")
        self.assertTrue(result)

    def test_send_ticket_confirmation(self):
        result = self.email_support.send_ticket_confirmation("test@example.com", "Test Event", "Test Ticket")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```