import os
import unittest
from unittest.mock import Mock, patch

from controller import app
from controller import cm
from data import ContentManager
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
  
    ###############
    #### tests ####
    ###############
 
    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Jiangren CMS" in response.get_data())
 
    @unittest.mock.patch('data.FlaskRedis')
    def test_get_content(self, mock_redis):
        redis_client = mock_redis.return_value
        redis_client.get.return_value = "My value"
        response = self.app.get('/content')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(), b"My value")
 
    @unittest.mock.patch('data.FlaskRedis')
    def test_set_content(self, mock_redis):
        payload = {'contentKey':'test_key', 'contentValue': 'test_value'}
        response = self.app.put('/content', data = payload)
        self.assertEqual(response.status_code, 200)
 
 
if __name__ == "__main__":
    unittest.main()