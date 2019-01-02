from .base import BaseTestCase
from app.auth.validations import validate_user_details


class TestUserTestCase(BaseTestCase):

    def test_auth_user_validation(self):
        """ Validate user details """
        data = {"email": "blairtony2014@gmail.com", 'password': 'codingmadefun2019', 'username' : 'tonyman'}
        user = validate_user_details(data)
        self.assertEqual(user, {})
