```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Importing shared dependencies
from shared_dependencies import userData, eventData, registrationConfirmation, ticketConfirmation, eventUpdate

def send_email(user_id, message_name):
    user = userData[user_id]
    event = eventData[user.event_id]
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = "noreply@virtualevents.com"
    msg['To'] = user.email
    msg['Subject'] = "Virtual Event Update"
    
    # Select the appropriate message based on the message_name
    if message_name == registrationConfirmation:
        body = f"Hello {user.name},\n\nYou have successfully registered for the event: {event.name}."
    elif message_name == ticketConfirmation:
        body = f"Hello {user.name},\n\nYour ticket for the event: {event.name} has been confirmed."
    elif message_name == eventUpdate:
        body = f"Hello {user.name},\n\nThere is an update for the event: {event.name}."
    else:
        body = "Hello {user.name},\n\nThis is a system generated email."

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    
    # Setup the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(msg['From'], "password")
    
    # Send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    server.quit()
```