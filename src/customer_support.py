```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from chatbot import ChatBot

class CustomerSupport:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.chatbot = ChatBot()

    def send_email(self, recipient_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        text = msg.as_string()
        server.sendmail(self.email, recipient_email, text)
        server.quit()

    def respond_to_query(self, query):
        response = self.chatbot.respond(query)
        return response

    def provide_updates(self, eventData, analyticsData):
        for organizer in eventData['organizers']:
            subject = "Event Update"
            message = f"Dear {organizer['name']},\n\nHere are the latest updates on your event:\n"
            for event in organizer['events']:
                message += f"\nEvent: {event['name']}\n"
                message += f"Attendees: {analyticsData[event['id']]['attendees']}\n"
                message += f"Engagement: {analyticsData[event['id']]['engagement']}\n"
            self.send_email(organizer['email'], subject, message)
```