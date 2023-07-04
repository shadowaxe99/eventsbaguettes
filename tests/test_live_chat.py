```python
import unittest
from src import live_chat

class TestLiveChat(unittest.TestCase):

    def setUp(self):
        self.live_chat = live_chat.LiveChat()
        self.user_data = {
            "username": "test_user",
            "email": "test_user@example.com"
        }

    def test_start_live_chat(self):
        response = self.live_chat.start_live_chat(self.user_data)
        self.assertEqual(response['status'], 'success')

    def test_send_message(self):
        message = "Hello, this is a test message."
        response = self.live_chat.send_message(self.user_data, message)
        self.assertEqual(response['status'], 'success')

    def test_receive_message(self):
        response = self.live_chat.receive_message(self.user_data)
        self.assertIsNotNone(response)

    def test_end_live_chat(self):
        response = self.live_chat.end_live_chat(self.user_data)
        self.assertEqual(response['status'], 'success')

if __name__ == '__main__':
    unittest.main()
```