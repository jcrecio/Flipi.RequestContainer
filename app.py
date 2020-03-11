from flask import Flask, request
from flight_request import FlightRequest
from flights_service import FlightsService
from json_encoder import JSONEncoder

app = Flask(__name__)
flightsService = FlightsService()

@app.route('/', methods = ['GET'])
def index():
    return "healthy"

@app.route('/requests', methods = ['GET'])
def get_flight_requests():
    return (flightsService.find_all(), 200, {'ContentType': 'application/json'})

@app.route('/requests', methods = ['POST'])
def insert_flight_request():
    insertedFlightId = flightsService.insert(request.get_json())
    return (insertedFlightId, 201, {'ContentType': 'application/json'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)