from platformcraft import *

import unittest.mock
from unittest.mock import patch

login = "zek0ffw0w"
password = "123456"

fake_auth_json = {'user_id': "uid", 'owner_id': "oid", 'access_token': "acces_tok", 'expires_at': 1, 'refresh_token': "ref_tok"}

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.auth = Auth("zek0ffw0w", "123456")

    def test_token_ok(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = fake_auth_json
            auth_info = self.auth.token("zek0ffw0w", "123456")

        self.assertEqual(auth_info.user_id, fake_auth_json["user_id"])

    def test_token_forbidden(self):

        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 403
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionForbidden) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    def test_refresh(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = fake_auth_json

            response = self.auth.refresh()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_auth_json)


if __name__ == '__main__':

    unittest.main()
