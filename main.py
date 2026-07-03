#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
import requests_cache
from dotenv import load_dotenv

import flight_data
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import serpapi

# ----------ENV VARIABLES ---------
load_dotenv()
requests_cache.install_cache('cache')
# Twilio SMS Messaging
TWILIO_SID=os.environ.get('TWILIO_SID')
TWILIO_TOKEN=os.environ.get('TWILIO_TOKEN')
TWILIO_NUMBER=os.environ.get('TWILIO_NUMBER')
TWILIO_TO_NUMBER=os.environ.get('TWILIO_TO_NUMBER')

# Build object and get data
DATA = DataManager()
sheet_data = DATA.get_data()

# Dates
from_time= datetime.today() + timedelta(days=1)
to_time = from_time + timedelta(days=6)
six_months=datetime.today()+relativedelta(months=+6)

# Build flight search object and search
SEARCH = FlightSearch()
from_place = 'LHR'
to_place = 'CDG'
print(SEARCH.flight_search(from_place, to_place, from_time=from_time, to_time=to_time,))
