```python
import unittest
from src import analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        self.analytics = analytics.Analytics()
        self.user_data = {"userId": 1, "name": "John Doe", "email": "johndoe@example.com"}
        self.event_data = {"eventId": 1, "eventName": "Virtual Concert", "eventDate": "2022-12-31"}

    def test_track_engagement(self):
        self.analytics.track_engagement(self.user_data, self.event_data)
        self.assertIn(self.user_data["userId"], self.analytics.analytics_data)
        self.assertIn(self.event_data["eventId"], self.analytics.analytics_data[self.user_data["userId"]])

    def test_get_event_analytics(self):
        self.analytics.track_engagement(self.user_data, self.event_data)
        event_analytics = self.analytics.get_event_analytics(self.event_data["eventId"])
        self.assertEqual(event_analytics["totalEngagement"], 1)

    def test_get_user_analytics(self):
        self.analytics.track_engagement(self.user_data, self.event_data)
        user_analytics = self.analytics.get_user_analytics(self.user_data["userId"])
        self.assertEqual(user_analytics["totalEventsAttended"], 1)

if __name__ == '__main__':
    unittest.main()
```