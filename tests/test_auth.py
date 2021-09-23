from ..auth import Auth
from ..exceptions import *

import unittest.mock

login = "zek0ffw0w"
password = "123456"


class TestAuth(unittest.TestCase):
    def setUp(self):
        pass

    def test_token_auth(self):
        with self.assertRaises(ExceptionAuth) as context:
            fake_login = "zek0ffw0w"
            fake_password = "1234"
            self.auth = Auth(fake_login, fake_password)
        self.assertTrue("login or password incorrect" in str(context.exception))

    def test_token_http(self):
        with self.assertRaises(ExceptionHTTPError) as context:
            self.auth = Auth(login, password)
            self.auth.AUTH_ADDR = "https://auth.platformcraft.r"
            self.auth.token(login, password)
        self.assertTrue("http post" in str(context.exception))

    def test_token_server(self):
        with self.assertRaises(ExceptionServerError) as context:
            self.auth = Auth(login, password)
            self.auth.AUTH_ADDR = "https://auth.platformcraft.ru/test"
            self.auth.token(login, password)
        self.assertTrue("unexpected response status" in str(context.exception))

    def test_refresh(self):
        with self.assertRaises(ExceptionRefresh) as context:
            self.auth = Auth(login, password)
            self.auth.user_id = "test312"
            self.auth.refresh()
        self.assertTrue("user id or access token or refresh token incorrect" in str(context.exception))

    def test_refresh_http(self):
        with self.assertRaises(ExceptionHTTPError) as context:
            self.auth = Auth(login, password)
            self.auth.AUTH_ADDR = "https://auth.platformcraft.r"
            self.auth.refresh()
        self.assertTrue("http post" in str(context.exception))

    def test_refresh_server(self):
        with self.assertRaises(ExceptionServerError) as context:
            self.auth = Auth(login, password)
            self.auth.AUTH_ADDR = "https://auth.platformcraft.ru/test"
            self.auth.refresh()
        self.assertTrue("unexpected response status" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
