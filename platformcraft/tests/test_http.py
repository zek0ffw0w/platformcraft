from platformcraft import *

import time

import unittest.mock
from unittest.mock import patch

login = "zek0ffw0w"
password = "123456"

fake_auth_json = {'user_id': "uid", 'owner_id': "oid", 'access_token': "acces_tok", 'expires_at': 1, 'refresh_token': "ref_tok"}
fake_file_info_json = {'id': "432drs", "status": "stat", "name": "name"}


class TestAuth(unittest.TestCase):

    def setUp(self):
        self.auth = Auth("zek0ffw0w", "123456")
        self.session = Session("zek0ffw0w", "123456")
        self.filespot = self.session.filespot()

    # testing post method
    def test_post_ok(self):
        with patch('platformcraft.http.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = fake_auth_json
            auth_info = self.auth.token("zek0ffw0w", "123456")

        self.assertEqual(auth_info.user_id, fake_auth_json["user_id"])

        time.sleep(1)

    def test_post_forbidden(self):
        with patch('platformcraft.http.requests.post') as mock_post:
            mock_post.return_value.status_code = 403
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionForbidden) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

        time.sleep(1)

    def test_post_bad_request(self):
        with patch('platformcraft.http.requests.post') as mock_post:
            mock_post.return_value.status_code = 400
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionBadRequest) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")

    time.sleep(1)

    def test_post_not_found(self):
        with patch('platformcraft.http.requests.post') as mock_post:
            mock_post.return_value.status_code = 404
            mock_post.return_value.ok = False
            mock_post.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionNotFound) as context:
                auth_info = self.auth.token("zek0ffw0w", "123456")
        time.sleep(1)

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

        time.sleep(1)

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

    # testing get method

    # def test_get_ok(self):
    #     with patch('platformcraft.http.requests.get') as mock_get:
    #         mock_get.return_value.status_code = 200
    #         mock_get.return_value.json.return_value = fake_file_info_json
    #         auth_info = self.filespot.file_info("test")
    #
    #     self.assertEqual(auth_info["id"], fake_file_info_json["id"])

    def test_get_forbidden(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 403
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionForbidden) as context:
                auth_info = self.filespot.file_info("test")

    def test_get_bad_request(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 400
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionBadRequest) as context:
                auth_info = self.filespot.file_info("test")
        time.sleep(1)

    def test_get_not_found(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 404
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionNotFound) as context:
                auth_info = self.filespot.file_info("test")

    def test_get_conflict(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 409
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionConflict) as context:
                auth_info = self.filespot.file_info("test")
        time.sleep(1)

    def test_get_too_many_requests(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 429
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionTooManyRequests) as context:
                auth_info = self.filespot.file_info("test")

    def test_get_internal_server_error(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 500
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionInternalServerError) as context:
                auth_info = self.filespot.file_info("test")
        time.sleep(1)

    def test_get_http_error(self):
        with patch('platformcraft.http.requests.get') as mock_get:
            mock_get.return_value.status_code = 502
            mock_get.return_value.ok = False
            mock_get.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionHTTPError) as context:
                auth_info = self.filespot.file_info("test")

        time.sleep(1)

    # testing put method

    # ok -

    def test_put_bad_request(self):
        with patch('platformcraft.http.requests.put') as mock_put:
            mock_put.return_value.status_code = 400
            mock_put.return_value.ok = False
            mock_put.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionBadRequest) as context:
                auth_info = self.filespot.change("test1", "1")
        time.sleep(1)

    def test_put_not_found(self):
        with patch('platformcraft.http.requests.put') as mock_put:
            mock_put.return_value.status_code = 404
            mock_put.return_value.ok = False
            mock_put.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionNotFound) as context:
                auth_info = self.filespot.change("test1", "1")

    def test_put_conflict(self):
        with patch('platformcraft.http.requests.put') as mock_put:
            mock_put.return_value.status_code = 409
            mock_put.return_value.ok = False
            mock_put.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionConflict) as context:
                auth_info = self.filespot.change("test1", "1")
        time.sleep(1)

    def test_put_too_many_requests(self):
        with patch('platformcraft.http.requests.put') as mock_put:
            mock_put.return_value.status_code = 429
            mock_put.return_value.ok = False
            mock_put.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionTooManyRequests) as context:
                auth_info = self.filespot.change("test1", "1")

    def test_put_internal_server_error(self):
        with patch('platformcraft.http.requests.put') as mock_put:
            mock_put.return_value.status_code = 500
            mock_put.return_value.ok = False
            mock_put.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionInternalServerError) as context:
                auth_info = self.filespot.change("test1", "1")
        time.sleep(1)

    def test_put_http_error(self):
        with patch('platformcraft.http.requests.put') as mock_put:
            mock_put.return_value.status_code = 502
            mock_put.return_value.ok = False
            mock_put.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionHTTPError) as context:
                auth_info = self.filespot.change("test1", "1")

    # testing delete method
    # ok -

    def test_delete_bad_request(self):
        with patch('platformcraft.http.requests.delete') as mock_delete:
            mock_delete.return_value.status_code = 400
            mock_delete.return_value.ok = False
            mock_delete.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionBadRequest) as context:
                auth_info = self.filespot.remove("test_11")
        time.sleep(1)

    def test_delete_not_found(self):
        with patch('platformcraft.http.requests.delete') as mock_delete:
            mock_delete.return_value.status_code = 404
            mock_delete.return_value.ok = False
            mock_delete.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionNotFound) as context:
                auth_info = self.filespot.remove("test_11")

    def test_delete_conflict(self):
        with patch('platformcraft.http.requests.delete') as mock_delete:
            mock_delete.return_value.status_code = 409
            mock_delete.return_value.ok = False
            mock_delete.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionConflict) as context:
                auth_info = self.filespot.remove("test_11")
        time.sleep(1)

    def test_delete_too_many_requests(self):
        with patch('platformcraft.http.requests.delete') as mock_delete:
            mock_delete.return_value.status_code = 429
            mock_delete.return_value.ok = False
            mock_delete.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionTooManyRequests) as context:
                auth_info = self.filespot.remove("test_11")

    def test_delete_internal_server_error(self):
        with patch('platformcraft.http.requests.delete') as mock_delete:
            mock_delete.return_value.status_code = 500
            mock_delete.return_value.ok = False
            mock_delete.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionInternalServerError) as context:
                auth_info = self.filespot.remove("test_11")
        time.sleep(1)

    def test_delete_http_error(self):
        with patch('platformcraft.http.requests.delete') as mock_delete:
            mock_delete.return_value.status_code = 502
            mock_delete.return_value.ok = False
            mock_delete.return_value.json.return_value = fake_auth_json

            with self.assertRaises(ExceptionHTTPError) as context:
                auth_info = self.filespot.remove("test_11")



if __name__ == '__main__':
    unittest.main()
