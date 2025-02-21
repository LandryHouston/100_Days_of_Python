import yaml
from twilio.rest import Client

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

TWILIO_ACCOUNT_SID = config['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = config['TWILIO_AUTH_TOKEN']
TWILIO_MESSAGING_SERVICE_ID = config['TWILIO_MESSAGING_SERVICE_ID']
TWILIO_VERIFIED_NUMBER = config['TWILIO_VERIFIED_NUMBER']

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            messaging_service_sid=TWILIO_MESSAGING_SERVICE_ID,
            body=message_body,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message)