
import unittest
from .base import BaseTestCase


class CommentApiTestCase(BaseTestCase):

    """ List comment api test"""
    def test_comments_api(self):
        response = self.client.post(
            '/api/v1/questions/answers/comment/1', data=self.data,
            headers={'Authorization': 'JWT ' + self.token}
        )
        assert response.status_code == 400


if __name__ == '__main__':
    unittest.main()