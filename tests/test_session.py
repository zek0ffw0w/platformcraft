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
        self.name = {'name': "test1", 'description': "test description", 'private': False}

    def test_post(self):
        with patch('platformcraft.session.requests.post') as mock_post:
            mock_post.return_value.status_code = 200

        response = self.session.post(url)
        self.assertEqual(response, 200)

    def test_get(self):
        with patch('platformcraft.session.requests.get') as mock_get:
            mock_get.return_value.status_code = 200

        response = self.session.get(url)
        self.assertEqual(response, 200)

    def test_put(self):
        with patch('platformcraft.session.requests.put') as mock_put:
            mock_put.return_value.status_code = 200
            pc_path = "test1"
            url_put = "https://filespot.platformcraft.ru/2/fs/container/" + self.session.owner_id + '/object/' + pc_path

        result_put = self.session.put(url_put, data=json.dumps(self.name))

        self.assertEqual(result_put.status_code, 200)

    def test_delete(self):
        with patch('platformcraft.session.requests.delete') as mock_delete:
            mock_delete.return_value.status_code = 200
        pc_path = "test_7"
        url_delete = "https://filespot.platformcraft.ru/2/fs/container/" + self.session.owner_id + '/object/'

        result_delete = self.session.delete(url_delete + pc_path)
        self.assertEqual(result_delete.status_code, 200)
        self.assertNotIn(pc_path, url_delete)


if __name__ == '__main__':
    unittest.main()
