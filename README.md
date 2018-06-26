
requirements for the project
-Visual Studio code as your code editor
-Python install
-Git install
-PostMan
-Install Lynting Library

Project source code setup
in the command prompt:
    cd into the project directory
    Create a virtual environment
    Activate the virtual environment


create a file(rides,tests)


In Rides
Import Flask
from flask import make_respons

create 2 Dictionaries(Rides and requests)
    write methods to GET all rides

    @app.route('/ridesapp/api/v1/rides', methods=['GET'])
    def get_rides():
    return jsonify({'rides': rides})


    GET a single ride
    @app.route('/ridesapp/api/v1/rides/<int:ride_id>', methods=['GET'])
    def get_ride(ride_id):
    ride = [ride for ride in rides if ride['id'] == ride_id]
    if len(ride) == 0:
        abort(404)
    return jsonify({'ride': ride[0]})   
    
     Edit(POST) a ride
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


     and a method to handle errors
     @app.errorhandler(404)
    def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    

    IN Tests
    import unittest
    from rides import app
Create a Class to Test all The APIs in File Rides
write a method to setup

def setUp(self):
        self.client = app.test_client()

method to test API "get all rides"
 def test_get_rides(self):
            res = self.client.get('/ridesapp/api/v1/rides')           
            result = json.loads(res.data.decode())          
            self.assertEqual(result['rides'][0]['NoPLate'], "UBA234F")
            self.assertEqual(res.status_code, 200)

method to test API "get a single rides"
    def test_get_single_ride(self):
            res = self.client.get('/ridesapp/api/v1/rides/3') 
            result = json.loads(res.data.decode())
            self.assertEqual(result['ride']['NoPLate'], "UBC235H")
            self.assertEqual(res.status_code, 200)        

method to test when the ride reuest is not found
    def test_get_ride_not_found(self):
            
            res = self.client.get('/ridesapp/api/v1/rides/100')     
            result = json.loads(res.data.decode())
            self.assertEqual(result['error'], "Not found")
            self.assertEqual(res.status_code, 404)



Creating the New Repo on git
go to github.com
create new repo and name it a name you prefer
go to the containing folder of the project
open in with "gitbush here"
In the command prompt:
    
    git status
    git add + "all the untracked the files you want to add" in the stage
    git remote add origin remote repository URL
    git commit -m 
    git push origin 
