
from flask import Flask, jsonify
from flask import abort
from flask import request
from flask import make_response
from flask import Request
import flask


app = Flask(__name__)

rides = [
    {
        'id': 1,
        'NoPLate': u'UBA234F',
        'destination': u'Makindye'
    },
    {
        'id': 2,
        'NoPLate': u'UBB214G',
        'destination': u'Mukono', 
        'done': False
    }

]

requests=[
    {
        'id': 1,
        'ride_id': 1,
        'destination': u'Makindye'
    }
]

#This the GET method to fetch all rides
@app.route('/ridesapp/api/v1/rides', methods=['GET'])
def get_rides():
    return jsonify({'rides': rides})

#This is the GET method to fetch a single ride
@app.route('/ridesapp/api/v1/rides/<int:ride_id>', methods=['GET'])
def get_ride(ride_id):
    ride = [ride for ride in rides if ride['id'] == ride_id]
    if len(ride) == 0:
        abort(404)
    return jsonify({'ride': ride[0]})   

#This is POST method to edit a ride
@app.route('/ridesapp/api/v1/rides', methods=['POST'])
def create_ride():
    if not request.json or not 'NoPLate' in request.json:
        abort(400)
    ride = {
        'id': rides[-1]['id'] + 1,
        'NoPLate': request.json['NoPLate'],
        'destination': request.json.get('destination'),
        'done': False
    }
    rides.append(ride)
    return jsonify({'ride': ride}), 201


#This is an error handler to give a better response for code 404!
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)


