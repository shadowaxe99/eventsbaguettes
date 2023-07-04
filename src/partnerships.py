```python
import requests
from src.analytics import analyticsData

class Partnership:
    def __init__(self, partner_name, partner_api):
        self.partner_name = partner_name
        self.partner_api = partner_api

    def get_partner_data(self):
        response = requests.get(self.partner_api)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def integrate_partner(self, eventData):
        partner_data = self.get_partner_data()
        if partner_data:
            for event in eventData:
                event['partners'] = partner_data.get(event['id'], [])
        return eventData

    def update_analytics(self):
        eventData = self.integrate_partner()
        analyticsData.update({'partnerships': self.partner_name})

def establish_partnership(partner_name, partner_api):
    partnership = Partnership(partner_name, partner_api)
    partnership.update_analytics()
    return partnership
```