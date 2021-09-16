import unittest
from unittest.mock import patch, mock_open
from session import *
import json

LOCAL_PATH = "C:/Users/malyc/Downloads/wiegand-produkte_en_1-710x368.mp4"
PC_PATH_INFO_TEST = "file_info_test"
PC_PATH_TEST = "upltest"
name = {'description': "TESTTTTT"}

LOGIN = "zek0ffw0w"
PASSWORD = "123456"


class TestFilespot(unittest.TestCase):
    def setUp(self):
        self.session = Session(LOGIN, PASSWORD)
        self.filespot = self.session.filespot()
        self.url = "https://filespot.platformcraft.ru/2/fs/container/" + self.session.owner_id + '/object/'

    def test_upload(self):
        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            assert open(LOCAL_PATH).read() == "data"
            mock_file.assert_called_with(LOCAL_PATH)

        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
        response = self.filespot.upload(LOCAL_PATH, PC_PATH_TEST)

        self.assertEqual(response.status_code, 200)
        # self.assertIn(PC_PATH_TEST, self.url)

    def test_remove(self):
        result_delete = self.filespot.remove(PC_PATH_TEST)
        self.assertEqual(result_delete.status_code, 200)
        self.assertNotIn(PC_PATH_TEST, self.url)

    def test_change(self):
        url_put = "https://filespot.platformcraft.ru/2/fs/container/" + self.session.owner_id + '/object/' + PC_PATH_INFO_TEST

        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = name

        result_put = self.session.put(url_put, data=json.dumps(name))
        result_info = self.filespot.file_info(PC_PATH_INFO_TEST)
        self.assertIn(list(name)[0], result_info.text)
        self.assertEqual(result_put.status_code, 200)

    def test_file_info(self):
        check_in = "duration"

        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = check_in

            filespot = self.session.filespot()
            response = filespot.file_info(PC_PATH_INFO_TEST)
        self.assertIn(check_in, response.text)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
