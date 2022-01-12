from platformcraft import *

import unittest.mock
from unittest.mock import patch

LOCAL_PATH = "platformcraft/tests/test_data/test.jpg"
LOCAL_PATH_FAKE = "fake_path"
PC_PATH_TEST1 = "test21"
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
        filespot.change.return_value.status_code = 404
        filespot.change.return_value.ok = False

        with self.assertRaises(ExceptionNotFound) as context:
            resp = filespot.change(PC_PATH_TEST3, description="43244")
            print(resp.status_code)


    # def test_file_info(self):
    #     # check normal behaviour
    #     with patch('platformcraft.filespot') as mock_file_info:
    #         mock_file_info.return_value.status_code = 200
    #         mock_file_info.return_value.ok = False
    #
    #         with self.assertRaises(ExceptionNotFound) as context:
    #             self.filespot = self.session.filespot()
    #             auth_info = self.filespot.file_info(PC_PATH_TEST2)
    #
    # def test_remove(self):
    #     # check normal behaviour
    #     self.filespot = self.session.filespot()
    #     response = self.filespot.remove(PC_PATH_TEST2)
    #
    #     self.assertEqual(response.status_code, 200)

    # def test_upload(self):
    #     # check normal behaviour
    #     self.filespot = self.session.filespot()
    #     response = self.filespot.upload(LOCAL_PATH, PC_PATH_TEST1)
    #
    #     self.assertEqual(response.status_code, 200)

    # def test_exception_open_file(self):
    #     with self.assertRaises(ExceptionOpenFile) as context:
    #         self.filespot = self.session.filespot()
    #         self.filespot.upload(LOCAL_PATH_FAKE, PC_PATH_TEST1, is_dir=False)
    #
    # def test_exception_server(self):
    #     with self.assertRaises(ExceptionNotFound) as context:
    #         self.filespot = self.session.filespot()
    #         params = {'name': "file_info_test", 'description': "test description", 'private': False}
    #         self.filespot.change(PC_PATH_TEST1, params)


if __name__ == '__main__':
    unittest.main()
