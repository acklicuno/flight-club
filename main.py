#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
import requests_cache
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from flight_data import FlightData
# ----------ENV VARIABLES ---------
load_dotenv()
requests_cache.install_cache('cache')
# Twilio SMS Messaging
TWILIO_SID=os.environ.get('TWILIO_SID')
TWILIO_TOKEN=os.environ.get('TWILIO_TOKEN')
TWILIO_NUMBER=os.environ.get('TWILIO_NUMBER')
TWILIO_TO_NUMBER=os.environ.get('TWILIO_TO_NUMBER')
# Build flight search object and search
SEARCH = FlightSearch()
# Build object and get data
DATA = DataManager()
sheet_data = DATA.get_data()
FLIGHT = FlightData()
# Build message object for twilio
TWILIO = NotificationManager()
# Dates
from_time= datetime.today() + timedelta(days=1)
to_time = from_time + timedelta(days=6)
six_months=datetime.today()+relativedelta(months=+6)
from_place = 'MDT'

# ----- COMPARE-------
# Iterate through each row(dict) in the sheet, and pull the IATA Code ----> into to_place
# call flight_search on every loop for each IATA Code
# Compare price in sheet dict, with price from discounted flight data\

def compare(sheet):
    sheety_header = {
        "Authorization": f"Bearer {os.environ.get('SHEETY_AUTH_HEADER')}",
    }
    updated_count = 0
    for row in sheet:
        to_place = row["iataCode"]
        flight_data = SEARCH.flight_search(from_place, to_place, from_time=from_time, to_time=to_time)
        combined = flight_data["best_flights"] + flight_data["other_flights"]
        discounted_flight_data = FLIGHT.find_cheapest_flight(combined)
        print(f"{row['city']}: sheet price ${row['price']}, live price ${discounted_flight_data['price']}")
        if discounted_flight_data["price"] < row["price"]:
            payload = {
                "sheet1": {
                    "Price": discounted_flight_data["price"]
                }
            }
            update_url =  f"{os.environ.get('SHEETY_END_POINT')}/{row['id']}"
            response = requests.put(url=update_url,json=payload, headers=sheety_header)
            print(response.status_code, response.text)
            updated_count += 1

            # Message user
            first_leg = discounted_flight_data["flights"][0]
            last_leg = discounted_flight_data["flights"][-1]
            TWILIO.message(discounted_flight_data["price"],
                    first_leg["departure_airport"]["id"],
                    last_leg["arrival_airport"]["id"],
                    first_leg["departure_airport"]["time"],
                    to_time.strftime("%Y-%m-%d"))
    return updated_count
completed = compare(sheet_data)
print(completed)