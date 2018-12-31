"test the base class"
import unittest
from app import create_app
from config import BaseConfig


app = create_app("config.BaseConfig")


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.data = {
            'username': 'tonieza',
            'email': 'blairtony1234@gmail.com',
            'password': 'gotsomethingtosmileabout',
            'database': BaseConfig.TEST_DB,
            'test_logout_token': None
        }
        """ Login to get a JWT token """
        self.client.post('/api/v1/auth/signup', json=self.data)
        response = self.client.post('/api/v1/auth/login', json=self.data)
        self.token = response.get_json().get('auth_token')
        self.user_id = '1'

    def tearDown(self):
        # method to invoke after each test. default to pass
        pass