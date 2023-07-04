```python
import unittest
from src.breakout_rooms import createBreakoutRoom

class TestBreakoutRooms(unittest.TestCase):

    def setUp(self):
        self.eventData = {
            "eventID": "123",
            "eventName": "AI Conference",
            "eventSchedule": {
                "startTime": "10:00",
                "endTime": "18:00",
                "date": "2022-12-12"
            },
            "breakoutRooms": []
        }

    def test_create_breakout_room(self):
        createBreakoutRoom(self.eventData, "AI Discussion", "10:30", "11:30")
        self.assertEqual(len(self.eventData["breakoutRooms"]), 1)
        self.assertEqual(self.eventData["breakoutRooms"][0]["name"], "AI Discussion")
        self.assertEqual(self.eventData["breakoutRooms"][0]["startTime"], "10:30")
        self.assertEqual(self.eventData["breakoutRooms"][0]["endTime"], "11:30")

if __name__ == '__main__':
    unittest.main()
```