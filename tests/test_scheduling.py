```python
import unittest
from src import scheduling

class TestScheduling(unittest.TestCase):

    def setUp(self):
        self.scheduling = scheduling.ScheduleEvent()

    def test_schedule_event(self):
        event_data = {
            "event_name": "AI Conference",
            "event_date": "2022-12-12",
            "event_time": "10:00",
            "event_duration": "2 hours",
            "event_speakers": ["Speaker 1", "Speaker 2"],
            "event_topics": ["AI in healthcare", "AI in finance"]
        }
        response = self.scheduling.schedule_event(event_data)
        self.assertEqual(response['status'], 'success')

    def test_invalid_event_data(self):
        event_data = {
            "event_name": "",
            "event_date": "2022-12-12",
            "event_time": "10:00",
            "event_duration": "2 hours",
            "event_speakers": ["Speaker 1", "Speaker 2"],
            "event_topics": ["AI in healthcare", "AI in finance"]
        }
        response = self.scheduling.schedule_event(event_data)
        self.assertEqual(response['status'], 'error')

    def test_event_overlap(self):
        event_data_1 = {
            "event_name": "AI Conference",
            "event_date": "2022-12-12",
            "event_time": "10:00",
            "event_duration": "2 hours",
            "event_speakers": ["Speaker 1", "Speaker 2"],
            "event_topics": ["AI in healthcare", "AI in finance"]
        }
        event_data_2 = {
            "event_name": "Data Science Conference",
            "event_date": "2022-12-12",
            "event_time": "10:30",
            "event_duration": "2 hours",
            "event_speakers": ["Speaker 3", "Speaker 4"],
            "event_topics": ["Data Science in healthcare", "Data Science in finance"]
        }
        self.scheduling.schedule_event(event_data_1)
        response = self.scheduling.schedule_event(event_data_2)
        self.assertEqual(response['status'], 'error')

if __name__ == '__main__':
    unittest.main()
```