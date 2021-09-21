from ..auth import Auth
from ..exceptions import *

import unittest.mock
from mock import patch

login = "zek0ffw0w"
password = "123456"


class TestAuth(unittest.TestCase):
    def setUp(self):
        self.auth = Auth(login, password)

    def test_token(self):
        fake_login = "zek0ffw0w"
        fake_password = "12345"
        with self.assertRaises(ExceptionAuth) as context:
            self.auth.token(fake_login, fake_password)
        self.assertTrue("login or password" in str(context.exception))

        # todo auth.ExceptionHTTPError, auth.ExceptionServerError
        # todo refresh.ExceptionRefresh, refresh.ExceptionHTTPError, refresh.ExceptionServerError

    # def test_token_1(self):
    #     fake_login = "zek0ffw0w"
    #     fake_password = "123456"
    #     with self.assertRaises(ExceptionHTTPError) as context:
    #         self.auth.token(fake_login, fake_password)
    #     self.assertTrue("http post" in str(context.exception))

    # def test_refresh(self):
    #     with self.assertRaises(ExceptionRefresh) as context:
    #         self.auth.refresh()
    #     self.assertTrue("user id or access" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
