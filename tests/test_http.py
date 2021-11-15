from platformcraft import *

import unittest.mock
from unittest.mock import patch

login = "zek0ffw0w"
password = "123456"

fake_auth_json = {'user_id': "uid", 'owner_id': "oid", 'access_token': "acces_tok", 'expires_at': 1, 'refresh_token': "ref_tok"}


class TestHttp(unittest.TestCase):

    def setUp(self):
        self.auth = Auth("zek0ffw0w", "123456")
        self.session = Session("zek0ffw0w", "123456")
        self.filespot = self.session.filespot()

    # testing method post

    def test_post_ok(self):
        with patch('platformcraft.http.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = fake_auth_json
            auth_info = self.auth.token("zek0ffw0w", "123456")

        self.assertEqual(auth_info.user_id, fake_auth_json["user_id"])

    def test_post_forbidden(self):
        with patch('platformcraft.http.requests.post') as mock_post:
            mock_post.return_value.status_code = 403
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionForbidden) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    def test_post_bad_request(self):
        with patch('platformcraft.http.requests.post') as mock_post:
            mock_post.return_value.status_code = 400
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionBadRequest) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    def test_post_not_found(self):
        with patch('platformcraft.http.requests.post') as mock_post:
            mock_post.return_value.status_code = 404
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionNotFound) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    def test_post_conflict(self):
        with patch('platformcraft.http.requests.post') as mock_post:
            mock_post.return_value.status_code = 409
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionConflict) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    def test_post_too_many_requests(self):
        with patch('platformcraft.http.requests.post') as mock_post:
            mock_post.return_value.status_code = 429
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionTooManyRequests) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    def test_post_internal_server_error(self):
        with patch('platformcraft.http.requests.post') as mock_post:
            mock_post.return_value.status_code = 500
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionInternalServerError) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    def test_post_http_error(self):
        with patch('platformcraft.http.requests.post') as mock_post:
            mock_post.return_value.status_code = 502
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionHTTPError) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    # testing method get

    def test_get_ok(self):
        with patch('platformcraft.http.requests.post') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = fake_auth_json
            auth_info = self.auth.token("zek0ffw0w", "123456")

        self.assertEqual(auth_info.user_id, fake_auth_json["user_id"])

    def test_get_forbidden(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 403
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionForbidden) as context:
                auth_info = self.filespot.file_info('test21')

    def test_get_bad_request(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 400
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionBadRequest) as context:
                auth_info = self.filespot.file_info('test21')

    def test_get_not_found(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 404
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionNotFound) as context:
                auth_info = self.filespot.file_info('test21')

    def test_get_conflict(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 409
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionConflict) as context:
                auth_info = self.filespot.file_info('test21')

    def test_get_too_many_requests(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 429
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionTooManyRequests) as context:
                auth_info = self.filespot.file_info('test21')

    def test_get_internal_server_error(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 500
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionInternalServerError) as context:
                auth_info = self.filespot.file_info('test21')

    def test_get_http_error(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 502
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionHTTPError) as context:
                auth_info = self.filespot.file_info('test21')