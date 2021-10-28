from platformcraft import *

import unittest.mock
from unittest.mock import patch, mock_open
import json

LOCAL_PATH = "platformcraft/tests/test_data/test.jpg"
LOCAL_PATH_FAKE = "fake_path"
PC_PATH_TEST1 = "test21"
PC_PATH_TEST2 = "test22"


LOGIN = "zek0ffw0w"
PASSWORD = "123456"


class TestFilespot(unittest.TestCase):
    def setUp(self):
        self.session = Session(LOGIN, PASSWORD)

    # def test_upload_file(self):
    #     with patch("builtins.open", mock_open(read_data="data")) as mock_file:
    #         assert open(LOCAL_PATH).read() == "data"
    #         mock_file.assert_called_with(LOCAL_PATH)

    def test_upload_file(self):
        # check normal behaviour
        self.filespot = self.session.filespot()
        self.filespot.upload(LOCAL_PATH, PC_PATH_TEST1)

    def test_change(self):
        # check normal behaviour
        self.filespot = self.session.filespot()
        params = {'name': PC_PATH_TEST2, 'description': "test description", 'private': False}
        self.filespot.change(PC_PATH_TEST1, params)

    def test_file_info(self):
        # check normal behaviour
        self.filespot = self.session.filespot()
        self.filespot.file_info(PC_PATH_TEST2)

    def test_remove(self):
        # check normal behaviour
        self.filespot = self.session.filespot()
        self.filespot.remove(PC_PATH_TEST2)

    def test_exception_open_file(self):
        with self.assertRaises(ExceptionOpenFile) as context:
            self.filespot = self.session.filespot()
            self.filespot.upload(LOCAL_PATH_FAKE, PC_PATH_TEST1)

    def test_exception_server(self):
        with self.assertRaises(ExceptionServerError) as context:
            self.filespot = self.session.filespot()
            params = {'name': "file_info_test", 'description': "test description", 'private': False}
            self.filespot.change(PC_PATH_TEST1, params)


if __name__ == '__main__':
    unittest.main()
