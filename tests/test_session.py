from ..session import *
from ..auth import *

import unittest
from mock import patch


login = "zek0ffw0w"
password = "123456"
url = "https://platformcraft.ru/"


class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session(login, password)
        self.name = {'name': "test_7", 'description': "test description", 'private': False}

    def test_post(self):
        with patch('session.requests.post') as mock_post:
            mock_post.return_value.status_code = 200

        response = self.session.post(url)
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        with patch('session.requests.get') as mock_get:
            mock_get.return_value.status_code = 200

        response = self.session.get(url)

        self.assertEqual(response.status_code, 200)

    def test_put(self):
        pc_path = "test_6"
        url_put = "https://filespot.platformcraft.ru/2/fs/container/" + self.session.owner_id + '/object/' + pc_path

        result_put = self.session.put(url_put, data=json.dumps(self.name))
        self.assertEqual(result_put.status_code, 200)

    def test_delete(self):
        pc_path = "test_7"
        url_delete = "https://filespot.platformcraft.ru/2/fs/container/" + self.session.owner_id + '/object/' + pc_path

        result_delete = self.session.delete(url_delete)
        self.assertEqual(result_delete.status_code, 200)


if __name__ == '__main__':
    unittest.main()
