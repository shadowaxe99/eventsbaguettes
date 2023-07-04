```python
import unittest
from src import networking

class TestNetworking(unittest.TestCase):

    def setUp(self):
        self.networking = networking.Network()

    def test_network_creation(self):
        self.assertIsNotNone(self.networking)

    def test_start_live_chat(self):
        user_id = "user123"
        self.networking.startLiveChat(user_id)
        self.assertIn(user_id, self.networking.liveChats)

    def test_create_breakout_room(self):
        room_id = "room123"
        self.networking.createBreakoutRoom(room_id)
        self.assertIn(room_id, self.networking.breakoutRooms)

    def test_network(self):
        user_id = "user123"
        self.networking.network(user_id)
        self.assertIn(user_id, self.networking.networkingUsers)

if __name__ == '__main__':
    unittest.main()
```