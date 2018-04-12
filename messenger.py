import datetime
from twilio.rest import Client
from config import TWILIO_ACCOUNT, TWILIO_TOKEN
twilio_client = Client(twilio_account, twilio_token)


class Messenger(object):

    def __init__(self):
        pass

    def send_reminder(self, notify_minutes):
        twilio_client.messages.create(to="+447871312430", from_="+447533046914",
                               body="Your next bus will be at your stop in " + str(notify_minutes) + ".")