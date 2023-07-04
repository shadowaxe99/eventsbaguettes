```python
import random
from datetime import datetime
from src.analytics import trackEngagement

class Ticket:
    def __init__(self, event_id, user_id, price):
        self.ticket_id = random.randint(1000, 9999)
        self.event_id = event_id
        self.user_id = user_id
        self.price = price
        self.purchase_time = datetime.now()

    def get_ticket_info(self):
        return {
            "ticket_id": self.ticket_id,
            "event_id": self.event_id,
            "user_id": self.user_id,
            "price": self.price,
            "purchase_time": self.purchase_time
        }

class TicketingSystem:
    def __init__(self):
        self.tickets = []

    def purchase_ticket(self, event_id, user_id, price):
        new_ticket = Ticket(event_id, user_id, price)
        self.tickets.append(new_ticket)
        trackEngagement("ticket_purchase", user_id, event_id)
        return new_ticket.get_ticket_info()

    def get_ticket(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket.get_ticket_info()
        return None

    def get_user_tickets(self, user_id):
        user_tickets = [ticket.get_ticket_info() for ticket in self.tickets if ticket.user_id == user_id]
        return user_tickets
```