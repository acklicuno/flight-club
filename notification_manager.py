import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

class NotificationManager:
    def __init__(self):
        self.SID = os.environ.get("TWILIO_SID")
        self.TOKEN = os.environ.get("TWILIO_TOKEN")
        self.TWILIO_BASE_NUMBER = os.environ.get("TWILIO_BASE_NUMBER")
        self.TWILIO_TO_NUMBER = os.environ.get("TWILIO_TO_NUMBER")

    def message(self,price, departure_iata, arrival_iata, outbound_date, inbound_date):
        client  = Client(self.SID, self.TOKEN)
        message = client.messages.create(
            body=f"Low Price Alert! Only ${price} to fly from {departure_iata} to {arrival_iata}, on {outbound_date} until {inbound_date}",
            from_=self.TWILIO_BASE_NUMBER,
            to=self.TWILIO_TO_NUMBER
        )