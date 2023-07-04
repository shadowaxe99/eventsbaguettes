```python
import unittest
from src.chatbot import Chatbot

class TestChatbot(unittest.TestCase):

    def setUp(self):
        self.chatbot = Chatbot()

    def test_resolve_issue(self):
        issue = "I can't register for the event"
        response = self.chatbot.resolve_issue(issue)
        self.assertEqual(response, "Please ensure you have filled all the required fields in the registration form.")

    def test_send_message(self):
        message = "What time does the event start?"
        response = self.chatbot.send_message(message)
        self.assertEqual(response, "The event starts at 10:00 AM.")

    def test_get_recommendations(self):
        user_data = {"interests": ["AI", "Networking"]}
        recommendations = self.chatbot.get_recommendations(user_data)
        self.assertIn("AI Session", recommendations)
        self.assertIn("Networking Session", recommendations)

if __name__ == '__main__':
    unittest.main()
```