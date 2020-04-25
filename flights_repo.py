from pymongo import MongoClient

class FlightsRepo:
    def __init__(self):

        try:
            # db_client = MongoClient("mongodb://requestcontainerdatabase:27017/", connectTimeoutMS=1000, socketTimeoutMS=1000)
            db_client = MongoClient("mongodb://requestcontainerdatabase:27017/")
        except:
            raise Exception("There was an error connecting to requester container godatabase")

        database = db_client.RequestContainer

        self.flightRequests = database.flightRequests

    def insert(self, flightRequest):
        result = self.flightRequests.insert_one(flightRequest)
        return str(result.inserted_id)

    def delete(self, flightRequestId):
        result = self.flightRequests.delete_one({ "_id": flightRequestId})
        return str(flightRequestId)

    def find_all(self):
        aggr = [ {'$replaceWith': { 'requestId': '$_id', 'from': '$from', 'to': '$to', 'maxPrice': '$maxPrice' } } ]
        return list(self.flightRequests.aggregate(aggr))