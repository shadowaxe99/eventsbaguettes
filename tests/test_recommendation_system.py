```python
import unittest
from src import recommendation_system

class TestRecommendationSystem(unittest.TestCase):

    def setUp(self):
        self.recommendation_system = recommendation_system.RecommendationSystem()
        self.userData = {"userId": 1, "interests": ["music", "technology", "networking"]}
        self.eventData = {"eventId": 1, "topics": ["music", "technology"]}

    def test_generate_recommendations(self):
        recommendations = self.recommendation_system.generate_recommendations(self.userData, self.eventData)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

    def test_update_user_profile(self):
        updated_user_data = self.recommendation_system.update_user_profile(self.userData, {"interests": ["art"]})
        self.assertIn("art", updated_user_data["interests"])

    def test_update_event_data(self):
        updated_event_data = self.recommendation_system.update_event_data(self.eventData, {"topics": ["art"]})
        self.assertIn("art", updated_event_data["topics"])

if __name__ == '__main__':
    unittest.main()
```