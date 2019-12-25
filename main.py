from flask import Flask, request
from flight_request import FlightRequest
from flights_repo import FlightsRepo
import json

from json_encoder import JSONEncoder


app = Flask(__name__)
flightsRepo = FlightsRepo()

@app.route('/')
def index():
    return 'Index!'

@app.route('/requests', methods = ['GET'])
def get_flight_requests():
    return (JSONEncoder().encode({ "flights": flightsRepo.find_all() }), 
        200, 
        {'ContentType': 'application/json'})

@app.route('/requests', methods = ['POST'])
def insert_flight_request():
    flightRequest = FlightRequest(request.json.get('name'))
    insertedFlightId = flightsRepo.insert(flightRequest)

    return (JSONEncoder().encode({ "id": insertedFlightId}), 201, {'ContentType': 'application/json'})

app.run(debug=True)