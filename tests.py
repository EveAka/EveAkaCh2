import unittest
import json
from rides import app
from copy import deepcopy


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_get_all_rides(self):
            res = self.client.get('/ridesapp/api/v1/rides')           
            result = json.loads(res.data.decode())          
            self.assertEqual(result['rides'][0]['NoPLate'], "UBA234F")
            self.assertEqual(res.status_code, 200)

    def test_get_a_single_ride(self):
            res = self.client.get('/ridesapp/api/v1/rides/1') 
            result = json.loads(res.data.decode())
            self.assertEqual(result['ride']['NoPLate'], "UBA234F")
            self.assertEqual(res.status_code, 200)        

    def test_get_ride_not_found(self):
            
            res = self.client.get('/ridesapp/api/v1/rides/100')     
            result = json.loads(res.data.decode())
            self.assertEqual(result['error'], "Not found")
            self.assertEqual(res.status_code, 404)


    def test_create_ride(self):  

            ride =  {
        'id': 1,
        'NoPLate': u'UBA234F'
        }
                          
            res = self.client.post('/ridesapp/api/v1/rides', data = json.dumps(ride),content_type = 'application/json')
            result = json.loads(res.data.decode())
            print(result)
            data = json.loads(res.get_data())
            self.assertEqual(data['ride']['NoPLate'], "UBA234F")
            self.assertEqual(res.status_code, 201)

#write a test on update ride
    def test_update_ride(self):
        
            
            ride ={
        'id': 2,
        'NoPLate': u'UBB214G',
        'destination': u'Mukono'
      
    }
            res = self.client.put('ridesapp/api/v1/rides/2',data=json.dumps(ride),content_type='application/json')                          
            self.assertEqual(res.status_code, 200)
            data = json.loads(res.get_data())
            self.assertEqual(data['ride']['NoPLate'], 'UBB214G')
            self.assertEqual(ride[2]['NoPLate'], 'UDE114D') 
    
#test on delete ride
    def test_delete_ride(self):
            res = self.client.delete('/ridesapp/api/v1/rides/3')#Good URL
            self.assertEqual(res.status_code, 200)
            res = self.client.delete('/ridesapp/api/v1/rides')#Bad URL
            self.assertEqual(res.status_code, 405)

#test on create request
    def test_create_request(self):  

            request =  {
                   
        'id': 1,
        'ride_id':1,
        'NoPLate': u'UBA234F',
        
        }
                       
            
            res = self.client.post('ridesapp/api/v1/requests', data = json.dumps(request),content_type = 'application/json')
            result = json.loads(res.data.decode())
            print(result)
            data = json.loads(res.get_data())
            self.assertEqual(data['ride']['NoPLate'], "UBA234F")
            self.assertEqual(res.status_code, 201)
    
#test on get all requests
    def test_get_all_requests(self):
            res = self.client.get('/ridesapp/api/v1/requests')           
            result = json.loads(res.data.decode())   
            print(result)       
            self.assertEqual(res.status_code, 200)

#test on get a single request
    def test_get_a_single_request(self):
            res = self.client.get('/ridesapp/api/v1/requests/1') 
            result = json.loads(res.data.decode())
            print(result)
            self.assertEqual(res.status_code, 200)        


#test on update request

#test on delete a request
def test_delete_request(self):
            res = self.client.delete('/ridesapp/api/v1/rides/request/1')#Good RideURL
            self.assertEqual(res.status_code, 200)
            
            res = self.client.delete('/ridesapp/api/v1/rides')#Bad RideURL
            self.assertEqual(res.status_code, 405)

   



    
  



        
               
        
if __name__ == "__main__": 

    unittest.main()