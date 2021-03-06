from flights_repo import FlightsRepo
from json_encoder import JSONEncoder

class FlightsService:
    def __init__(self):
        self.flightsRepo = FlightsRepo()

    def find_all(self):
        return JSONEncoder().encode(self.flightsRepo.find_all())

    def insert(self, flightRequest):
        insertedFlightId = self.flightsRepo.insert(flightRequest)
        return JSONEncoder().encode({ "_id": insertedFlightId})

    def delete(self, flightRequestId):
        deletedFlightId = self.flightsRepo.delete(flightRequestId)
        return JSONEncoder().encode({ "_id": deletedFlightId})