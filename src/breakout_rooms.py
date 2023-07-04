```python
import random
from src.analytics import trackEngagement

class BreakoutRoom:
    def __init__(self, room_id, event_id):
        self.room_id = room_id
        self.event_id = event_id
        self.participants = []

    def add_participant(self, user):
        self.participants.append(user)
        trackEngagement('breakout_room_join', user, self.event_id)

    def remove_participant(self, user):
        self.participants.remove(user)
        trackEngagement('breakout_room_leave', user, self.event_id)

def createBreakoutRoom(event_id):
    room_id = random.randint(1000, 9999)
    new_room = BreakoutRoom(room_id, event_id)
    return new_room
```