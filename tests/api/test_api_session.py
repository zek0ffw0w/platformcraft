from platformcraft import *

import unittest

login = "zek0ffw0w"
password = "123456"


class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session(login, password)
        self.url = "https://filespot.platformcraft.ru"

    def test_post_serv(self):
        with self.assertRaises(ExceptionServerError) as context:
            self.url = "https://filespot.platformcraft.ru"
            self.session.post(self.url)
        self.assertTrue("unexpected response status" in str(context.exception))

    def test_post_http(self):
        with self.assertRaises(ExceptionHTTPError) as context:
            self.url = "https://auth.platformcraft.r"
            self.session.post(self.url)
        self.assertTrue("http post:" in str(context.exception))

    def test_get_serv(self):
        with self.assertRaises(ExceptionServerError) as context:
            self.url = "https://filespot.platformcraft.ru"
            self.session.get(self.url)
        self.assertTrue("unexpected response status" in str(context.exception))

    def test_get_http(self):
        with self.assertRaises(ExceptionHTTPError) as context:
            self.url = "https://auth.platformcraft.r"
            self.session.get(self.url)
        self.assertTrue("http get error:" in str(context.exception))

    def test_put_serv(self):
        with self.assertRaises(ExceptionServerError) as context:
            self.url = "https://filespot.platformcraft.ru"
            self.session.put(self.url)
        self.assertTrue("unexpected response status" in str(context.exception))

    def test_put_http(self):
        with self.assertRaises(ExceptionHTTPError) as context:
            self.url = "https://auth.platformcraft.r"
            self.session.put(self.url)
        self.assertTrue("http put error:" in str(context.exception))

    def test_delete_serv(self):
        with self.assertRaises(ExceptionServerError) as context:
            self.url = "https://filespot.platformcraft.ru"
            self.session.delete(self.url)
        self.assertTrue("unexpected response status" in str(context.exception))

    def test_delete_http(self):
        with self.assertRaises(ExceptionHTTPError) as context:
            self.url = "https://auth.platformcraft.r"
            self.session.delete(self.url)
        self.assertTrue("http delete error:" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
