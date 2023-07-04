```python
import unittest
from src import automation_tools

class TestAutomationTools(unittest.TestCase):

    def setUp(self):
        self.automation_tools = automation_tools.AutomationTools()

    def test_registerUser(self):
        user_data = {"name": "John Doe", "email": "johndoe@example.com"}
        response = self.automation_tools.registerUser(user_data)
        self.assertEqual(response['message'], 'User registered successfully')

    def test_purchaseTicket(self):
        ticket_data = {"eventId": "123", "userId": "456"}
        response = self.automation_tools.purchaseTicket(ticket_data)
        self.assertEqual(response['message'], 'Ticket purchased successfully')

    def test_scheduleEvent(self):
        event_data = {"name": "Virtual Concert", "date": "2022-12-31", "time": "20:00"}
        response = self.automation_tools.scheduleEvent(event_data)
        self.assertEqual(response['message'], 'Event scheduled successfully')

    def test_startLiveChat(self):
        chat_data = {"eventId": "123", "userId": "456"}
        response = self.automation_tools.startLiveChat(chat_data)
        self.assertEqual(response['message'], 'Live chat started successfully')

    def test_createBreakoutRoom(self):
        room_data = {"eventId": "123", "roomName": "Networking Room 1"}
        response = self.automation_tools.createBreakoutRoom(room_data)
        self.assertEqual(response['message'], 'Breakout room created successfully')

    def test_network(self):
        network_data = {"eventId": "123", "userId": "456"}
        response = self.automation_tools.network(network_data)
        self.assertEqual(response['message'], 'Networking started successfully')

    def test_trackEngagement(self):
        engagement_data = {"eventId": "123", "userId": "456"}
        response = self.automation_tools.trackEngagement(engagement_data)
        self.assertEqual(response['message'], 'Engagement tracked successfully')

    def test_resolveIssue(self):
        issue_data = {"eventId": "123", "userId": "456", "issue": "Cannot join breakout room"}
        response = self.automation_tools.resolveIssue(issue_data)
        self.assertEqual(response['message'], 'Issue resolved successfully')

if __name__ == '__main__':
    unittest.main()
```