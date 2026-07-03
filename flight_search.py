import os
import requests
from dotenv import load_dotenv
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key=os.environ.get('SERP_API_KEY')
        self.api_endpoint=os.environ.get('SERP_END_POINT')
        self.SERP_PARAMS = {}

    def flight_search(self,origin_city_code, destination_city_code, from_time, to_time):
        self.SERP_PARAMS = {
            "engine":"google_flights",
            "departure_id":origin_city_code,
            "arrival_id":destination_city_code,
            "outbound_date":from_time.strftime("%Y-%m-%d"),
            "return_date":to_time.strftime("%Y-%m-%d"),
            "api_key":self.api_key
        }
        response=requests.get(self.api_endpoint,params=self.SERP_PARAMS)
        return response.json()