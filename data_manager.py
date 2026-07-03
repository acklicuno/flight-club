import requests
import os
from dotenv import load_dotenv
load_dotenv()

class DataManager:

    def __init__(self):
        self.SHEETY_END_POINT = os.environ.get('SHEETY_END_POINT')
        self.SHEET_AUTH_HEADER = os.environ.get('SHEETY_AUTH_HEADER')
        self.HEADER_PARAMS = {"Authorization": f"Bearer {self.SHEET_AUTH_HEADER}"}
        self.SHEET_DATA = None

    def get_data(self):
        self.SHEET_DATA = requests.get(self.SHEETY_END_POINT, headers=self.HEADER_PARAMS)
        return self.SHEET_DATA.json()["sheet1"]