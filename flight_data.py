
class FlightData:
    def __init__(self):
        self.cheapest = None

    @staticmethod
    def find_cheapest_flight(data, return_date):
        cheapest = min(data, key=lambda x: x["price"])
        first_leg = cheapest["flights"][0]
        departure_airport = first_leg["departure_airport"]["name"]
        arrival_airport = first_leg["arrival_airport"]["name"]
        departure_time = first_leg["departure_airport"]["time"]
        return cheapest, departure_airport, arrival_airport, departure_time