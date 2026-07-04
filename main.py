#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
import requests_cache
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
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
DATA = FlightData()
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
    for row in sheet:
        to_place = row["iataCode"]
        flight_data = SEARCH.flight_search(from_place, to_place, from_time=from_time, to_time=to_time)
        # combined = flight_data["best_flights"] + flight_data["other_flights"]
        discounted_flight_data = DATA.find_cheapest_flight(new_data)
        if discounted_flight_data["price"] < row["price"]:
            # Alter data in sheet
            # Do full twilio stuff
    return

# Parse Data from flightsearch, and pass tow flightdata to filter and return cheapest flight
new_data = compare(sheet_data)
