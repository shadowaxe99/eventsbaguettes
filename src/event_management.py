```python
import datetime
from src.registration import registerUser
from src.ticketing import purchaseTicket
from src.scheduling import scheduleEvent

class Event:
    def __init__(self, name, description, date, time, location):
        self.name = name
        self.description = description
        self.date = date
        self.time = time
        self.location = location
        self.attendees = []

    def add_attendee(self, user):
        self.attendees.append(user)

class EventManagement:
    def __init__(self):
        self.events = []
        self.eventData = {}

    def create_event(self, name, description, date, time, location):
        new_event = Event(name, description, date, time, location)
        self.events.append(new_event)
        self.eventData[name] = {
            'description': description,
            'date': date,
            'time': time,
            'location': location,
            'attendees': []
        }

    def register_user_to_event(self, user, event_name):
        for event in self.events:
            if event.name == event_name:
                registerUser(user)
                event.add_attendee(user)
                self.eventData[event_name]['attendees'].append(user)
                return f"User {user} has been registered to the event {event_name}"

    def purchase_ticket_for_event(self, user, event_name):
        for event in self.events:
            if event.name == event_name:
                purchaseTicket(user, event_name)
                return f"User {user} has purchased a ticket for the event {event_name}"

    def schedule_event(self, event_name, date, time):
        for event in self.events:
            if event.name == event_name:
                scheduleEvent(event_name, date, time)
                self.eventData[event_name]['date'] = date
                self.eventData[event_name]['time'] = time
                return f"The event {event_name} has been scheduled on {date} at {time}"
```