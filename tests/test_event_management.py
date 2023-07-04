```python
import unittest
from src import event_management

class TestEventManagement(unittest.TestCase):

    def setUp(self):
        self.event_management = event_management.EventManagement()

    def test_registerUser(self):
        user_data = {"name": "John Doe", "email": "johndoe@example.com"}
        response = self.event_management.registerUser(user_data)
        self.assertEqual(response, "registrationConfirmation")

    def test_purchaseTicket(self):
        ticket_data = {"event_id": 1, "user_id": 1}
        response = self.event_management.purchaseTicket(ticket_data)
        self.assertEqual(response, "ticketConfirmation")

    def test_scheduleEvent(self):
        event_data = {"name": "AI Conference", "date": "2022-12-31", "location": "Virtual"}
        response = self.event_management.scheduleEvent(event_data)
        self.assertEqual(response, "eventUpdate")

    def test_startLiveChat(self):
        chat_data = {"user_id": 1, "message": "Hello, world!"}
        response = self.event_management.startLiveChat(chat_data)
        self.assertEqual(response, "liveChat")

    def test_createBreakoutRoom(self):
        room_data = {"event_id": 1, "name": "AI Discussion"}
        response = self.event_management.createBreakoutRoom(room_data)
        self.assertEqual(response, "breakoutRoom")

    def test_network(self):
        network_data = {"user_id": 1, "event_id": 1}
        response = self.event_management.network(network_data)
        self.assertEqual(response, "networkingPlatform")

    def test_trackEngagement(self):
        engagement_data = {"user_id": 1, "event_id": 1, "engagement_score": 85}
        response = self.event_management.trackEngagement(engagement_data)
        self.assertEqual(response, "analyticsData")

    def test_resolveIssue(self):
        issue_data = {"user_id": 1, "issue": "Unable to join event"}
        response = self.event_management.resolveIssue(issue_data)
        self.assertEqual(response, "issueResolution")

if __name__ == '__main__':
    unittest.main()
```