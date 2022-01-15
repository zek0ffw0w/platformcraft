from platformcraft import *

import unittest.mock
from unittest.mock import patch

LOCAL_PATH = "platformcraft/tests/test_data/test.jpg"
LOCAL_PATH_FAKE = "fake_path"
PC_PATH_TEST1 = "test213"
PC_PATH_TEST2 = "test22"
PC_PATH_TEST3 = "c333"
FILESPOT_ADDR = "https://filespot.platformcraft.ru/2/fs/container/"
params = {'name': "file_info_test", 'description': "test description", 'private': False}
LOGIN = "zek0ffw0w"
PASSWORD = "123456"


class TestFilespot(unittest.TestCase):
    session = Session(LOGIN, PASSWORD)

    @patch('platformcraft.filespot')
    def test_change(self, MockChange):
        filespot = MockChange()
        filespot.change(PC_PATH_TEST1, name=PC_PATH_TEST1, description="33", private=False)

    @patch('platformcraft.filespot')
    def test_file_info(self, MockInfo):
        filespot = MockInfo()
        filespot.file_info(PC_PATH_TEST1)

    @patch('platformcraft.filespot')
    def test_remove(self, MockRemove):
        filespot = MockRemove()
        filespot.remove(PC_PATH_TEST1)

    @patch('platformcraft.filespot')
    def test_upload(self, MockUpload):
        filespot = MockUpload()
        filespot.upload(PC_PATH_TEST1, PC_PATH_TEST2)

    def test_exception_open_file(self):
        with self.assertRaises(ExceptionOpenFile) as context:
            self.filespot = self.session.filespot()
            self.filespot.upload(LOCAL_PATH_FAKE, PC_PATH_TEST1, is_dir=False)

    def test_exception_server(self):
        with self.assertRaises(ExceptionNotFound) as context:
            self.filespot = self.session.filespot()
            self.filespot.change(PC_PATH_TEST1, name=PC_PATH_TEST1, description="33", private=False)


if __name__ == '__main__':
    unittest.main()
