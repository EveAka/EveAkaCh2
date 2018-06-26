import unittest
import json
from rides import app
from copy import deepcopy


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_get_rides(self):
            res = self.client.get('/ridesapp/api/v1/rides')           
            result = json.loads(res.data.decode())          
            self.assertEqual(result['rides'][0]['NoPLate'], "UBA234F")
            self.assertEqual(res.status_code, 200)

    def test_get_single_ride(self):
            res = self.client.get('/ridesapp/api/v1/rides/3') 
            result = json.loads(res.data.decode())
            self.assertEqual(result['ride']['NoPLate'], "UBC235H")
            self.assertEqual(res.status_code, 200)        

    def test_get_ride_not_found(self):
            
            res = self.client.get('/ridesapp/api/v1/rides/100')     
            result = json.loads(res.data.decode())
            self.assertEqual(result['error'], "Not found")
            self.assertEqual(res.status_code, 404)
                   
    
        
               
        
if __name__ == "__main__": 

    unittest.main()