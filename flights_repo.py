from pymongo import MongoClient

class FlightsRepo:
    def __init__(self):
        db_client = MongoClient()
        database = db_client.RequestContainer

        self.flightRequests = database.flightRequests

    def insert(self, flightRequest):
        result = self.flightRequests.insert_one(flightRequest.toJSON())
        return str(result.inserted_id)

    def find_all(self):
        return list(self.flightRequests.find({}))

#     def find_one(self):