import unittest
from unittest.mock import patch, mock_open
from session import *
from filespot import *
import json

LOCAL_PATH = "C:/Users/malyc/Downloads/wiegand-produkte_en_1-710x368.mp4"
PC_PATH = "file_info_test"
LOGIN = "zek0ffw0w"
PASSWORD = "123456"
url = "https://platformcraft.ru/"


class TestFilespot(unittest.TestCase):
    def setUp(self):
        self.session = Session(LOGIN, PASSWORD)

    def test_upload(self):
        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            assert open(LOCAL_PATH).read() == "data"
            mock_file.assert_called_with(LOCAL_PATH)

        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200

        response = self.session.post(url)
        self.assertEqual(response.status_code, 200)

    # def test_remove(self):
    #     pass
    #
    # def test_change(self):
    #     pass

    # todo test_file_info(?), test_remove, test_cchange

    def test_file_info(self):
        fake_json = "download_url"

        with patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = fake_json

            filespot = self.session.filespot()
            response = filespot.file_info(PC_PATH)
            # print(response.text)

        self.assertIn(fake_json, response.text)
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
