
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
      
    },
    {
        'id': 3,
        'NoPLate': u'UBC235H',
        'destination': u'Mukono', 

    }
    

]

requests=[
    {
       'id': 1,
        'ride_id': 1,
        'destination': u'Makindye',
        'NoPLate': u'UBA234F'
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

#This is POST method to create a new ride
@app.route('/ridesapp/api/v1/rides', methods=['POST'])
def create_ride():
    if not request.json or not 'NoPLate' in request.json:
        abort(400)
    ride = {
        'id': rides[-1]['id'] + 1,
        'NoPLate': request.json['NoPLate'],
        'destination': request.json.get('destination')
        
    }
    rides.append(ride)
    return jsonify({'ride': ride}), 201

#method to edit a ride
@app.route('/ridesapp/api/v1/rides', methods=['PUT'])
def update_ride(ride_id):
    ride = [ride for ride in ride if ride['id'] == ride_id]
    if len(ride) == 0:
        abort(404)
    if not request.json:
        abort(400)
    ride[0]['NoPLate'] = request.json.get('NoPLate', ride[0]['NoPLate'])
    ride[0]['destination'] = request.json.get('destination', ride[0]['destination'])
    return jsonify({'ride': ride[0]})
    
#This is a DELETE Method
@app.route('/ridesapp/api/v1/rides/<int:ride_id>', methods=['DELETE'])
def delete_ride(ride_id):
    ride = [ride for ride in rides if ride['id'] == ride_id]
    if len(ride) == 0:
        abort(404)
    rides.remove(ride[0])
    return jsonify({'result': True}) 

#Write a method here to create a request 
@app.route('/ridesapp/api/v1/rides/<int:ride_id>/requests', methods=['POST'])
def create_request(ride_id):
    ride = [ride for ride in rides if ride['id'] == ride_id]
    if ride :
    
        request = {
            'id': requests[-1]['id'] + 1,
            'destination': flask.request.json.get('destination'),
            'ride_id': ride_id
        
        }
        requests.append(request)
        return jsonify({'request': request}), 201
    else:
        return("Ride Id doesnt exist")    
#Write a method here to get all requests
@app.route('/ridesapp/api/v1/requests', methods=['GET'])
def get_all_requests():
    return jsonify({'requests': requests})

#Write a method here to get a single request
@app.route('/ridesapp/api/v1/requests/<int:request_id>', methods=['GET'])
def get_a_single_request(request_id):
    my_req = [req for req in requests if req['id'] == request_id] # loop through the requests to check for the requestid
    if len(my_req) == 0:
        abort(404)
    return jsonify({'request': my_req[0]})

#Write a method here to update a request 
@app.route('/ridesapp/api/v1/requests/<int:request_id>', methods=['PUT'])
def update_request(request_id):
    my_req = [req for req in requests if req['id'] == request_id]
    if len(my_req) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'NoPlate' not in request.json:
        abort(400)
    my_req[0]['NoPlate'] = request.json.get('NoPlate', my_req[0]['NoPlate'])
    return jsonify({'request': my_req[0]})  

#method to delete a request 
@app.route('/ridesapp/api/v1/requests/<int:request_id>', methods=['DELETE'])
def delete_request(request_id):
    my_req = [req for req in requests if req['id'] == request_id]
    if len(my_req) == 0:
        abort(404)
    requests.remove(my_req[0])
    return jsonify({'request': my_req[0]})

#This is an error handler to give a better response for code 404!
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)


