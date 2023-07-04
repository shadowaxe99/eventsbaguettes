```python
from src.user_schema import UserSchema
from src.event_schema import EventSchema
from src.analytics import trackEngagement

class Registration:
    def __init__(self):
        self.user_data = []
        self.event_data = []

    def registerUser(self, user_info, event_id):
        user_schema = UserSchema()
        event_schema = EventSchema()

        if user_schema.validate(user_info) and event_schema.validate_id(event_id):
            user_info['event_id'] = event_id
            self.user_data.append(user_info)
            trackEngagement('registration', user_info)
            return 'registrationConfirmation'
        else:
            return 'Error: Invalid user info or event id'

    def getRegisteredUsers(self, event_id):
        registered_users = [user for user in self.user_data if user['event_id'] == event_id]
        return registered_users
```