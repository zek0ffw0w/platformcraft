from platformcraft import *

import unittest.mock
from unittest.mock import patch, mock_open
import json

LOCAL_PATH = "platformcraft/tests/test_data/test.jpg"
LOCAL_PATH_FAKE = "fake_path"
PC_PATH_INFO_TEST = "file_info_test"
PC_PATH_TEST = "upltest1"


LOGIN = "zek0ffw0w"
PASSWORD = "123456"


class TestFilespot(unittest.TestCase):
    def setUp(self):
        self.session = Session(LOGIN, PASSWORD)

    # def test_upload_file(self):
    #     with patch("builtins.open", mock_open(read_data="data")) as mock_file:
    #         assert open(LOCAL_PATH).read() == "data"
    #         mock_file.assert_called_with(LOCAL_PATH)

    def test_upload_open_file(self):
        with self.assertRaises(ExceptionOpenFile) as context:
            self.filespot = self.session.filespot()
            self.filespot.FILESPOT_ADDR = "https://filespot.platformcraft.ru/2/fs/containe/"
            self.filespot.upload(LOCAL_PATH_FAKE, PC_PATH_TEST)
        self.assertTrue("cant open file" in str(context.exception))

    def test_upload_file(self):
        with self.assertRaises(ExceptionUpload) as context:
            self.filespot = self.session.filespot()
            self.filespot.FILESPOT_ADDR = "https://filespot.platformcraft.ru/2/fs/containe/"
            self.filespot.upload(LOCAL_PATH, PC_PATH_TEST)
        self.assertTrue("cant upload file" in str(context.exception))

# todo check for file_remove not in storage?
    def test_remove(self):
        with self.assertRaises(ExceptionRemove) as context:
            self.filespot = self.session.filespot()
            self.filespot.FILESPOT_ADDR = "https://filespot.platformcraft.ru/2/fs/containe/"
            self.filespot.remove(PC_PATH_TEST)
        self.assertTrue("cant remove file" in str(context.exception))

    def test_change(self):
        with self.assertRaises(ExceptionChange) as context:
            self.filespot = self.session.filespot()
            self.filespot.FILESPOT_ADDR = "https://filespot.platformcraft.ru/2/fs/containe/"
            params = {'name': "file_info_test", 'description': "test description", 'private': False}
            self.filespot.change(PC_PATH_INFO_TEST, params)
        self.assertTrue("cant change file" in str(context.exception))

    def test_file_info(self):
        with self.assertRaises(ExceptionInfo) as context:
            self.filespot = self.session.filespot()
            self.filespot.FILESPOT_ADDR = "https://filespot.platformcraft.ru/2/fs/container/"
            self.filespot.file_info(PC_PATH_TEST)
        self.assertTrue("cant get file info" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
