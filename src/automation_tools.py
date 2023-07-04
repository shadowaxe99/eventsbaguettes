```python
import datetime
from src.registration import registerUser
from src.ticketing import purchaseTicket
from src.scheduling import scheduleEvent

class AutomationTools:
    def __init__(self, eventData, userData):
        self.eventData = eventData
        self.userData = userData

    def automateRegistration(self, user):
        registrationStatus = registerUser(user, self.userData)
        if registrationStatus:
            print("User registration automated successfully.")
        else:
            print("User registration automation failed.")

    def automateTicketing(self, user, event):
        ticketStatus = purchaseTicket(user, event, self.eventData)
        if ticketStatus:
            print("Ticket purchase automated successfully.")
        else:
            print("Ticket purchase automation failed.")

    def automateScheduling(self, event):
        scheduleStatus = scheduleEvent(event, self.eventData)
        if scheduleStatus:
            print("Event scheduling automated successfully.")
        else:
            print("Event scheduling automation failed.")

    def automateEventManagement(self, user, event):
        self.automateRegistration(user)
        self.automateTicketing(user, event)
        self.automateScheduling(event)
        print("Event management automation completed.")
```