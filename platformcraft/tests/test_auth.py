from platformcraft import *

import unittest.mock
from unittest.mock import patch

login = "zek0ffw0w"
password = "123456"

fake_auth_json = {'user_id': "uid", 'owner_id': "oid", 'access_token': "acces_tok", 'expires_at': 1, 'refresh_token': "ref_tok"}


class TestAuth(unittest.TestCase):
    auth = Auth("zek0ffw0w", "123456")

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

    def test_token_bad_request(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 400
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionBadRequest) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    def test_token_not_found(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 404
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionNotFound) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    def test_token_conflict(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 409
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionConflict) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    def test_token_too_many_requests(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 429
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionTooManyRequests) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    def test_token_internal_server_error(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionInternalServerError) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    def test_token_http_error(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 502
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionHTTPError) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    # testing method refresh

    def test_refresh_ok(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = fake_auth_json
            auth_info = self.auth.refresh()

        self.assertEqual(auth_info.user_id, fake_auth_json["user_id"])

    def test_refresh_forbidden(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 403
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionForbidden) as context:
                auth_info = self.auth.refresh()

    def test_refresh_bad_request(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 400
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionBadRequest) as context:
                auth_info = self.auth.refresh()

    def test_refresh_not_found(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 404
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionNotFound) as context:
                auth_info = self.auth.refresh()

    def test_refresh_conflict(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 409
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionConflict) as context:
                auth_info = self.auth.refresh()

    def test_refresh_too_many_requests(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 429
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionTooManyRequests) as context:
                auth_info = self.auth.refresh()

    def test_refresh_internal_server_error(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionInternalServerError) as context:
                auth_info = self.auth.refresh()

    def test_refresh_http_error(self):
        with patch('platformcraft.auth.requests.post') as mock_post:
            mock_post.return_value.status_code = 502
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionHTTPError) as context:
                auth_info = self.auth.refresh()


if __name__ == '__main__':
    unittest.main()
