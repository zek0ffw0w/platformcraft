import unittest
from mock import patch
from auth import Auth

login = "zek0ffw0w"
password = "123456"


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.auth = Auth("zek0ffw0w", "123456")

    def test_token(self):
        fake_json = {'user_id': "611a5c4ccd0a6b6c94c5a3da", 'owner_id': "", 'access_token': "12", 'expires_at': "432", 'refresh_token': "432"}

        with patch('auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = fake_json

            response = self.auth.token("zek0ffw0w", "123456")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_json)

    def test_refresh(self):
        fake_json = {'user_id': "611a5c4ccd0a6b6c94c5a3da", 'owner_id': "1", 'access_token': "12", 'expires_at': "432", 'refresh_token': "432"}

        with patch('auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = fake_json

            response = self.auth.refresh()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), fake_json)


if __name__ == '__main__':
    unittest.main()
