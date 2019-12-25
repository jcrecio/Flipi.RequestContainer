from flights_repo import FlightsRepo
from json_encoder import JSONEncoder

class FlightsService:
    def __init__(self):
        self.flightsRepo = FlightsRepo()

    def find_all(self):
        return JSONEncoder().encode({ "flights": self.flightsRepo.find_all() })

    def insert(self, flightRequest):
        insertedFlightId = self.flightsRepo.insert(flightRequest)
        return JSONEncoder().encode({ "id": insertedFlightId})