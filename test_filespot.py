import unittest
from unittest.mock import patch, mock_open
from session import *
from filespot import *

LOCAL_PATH = "C:/Users/malyc/Downloads/wiegand-produkte_en_1-710x368.mp4"
PC_PATH = "vidik"
LOGIN = "zek0ffw0w"
PASSWORD = "123456"


class TestFilespot(unittest.TestCase):
    def setUp(self):
        self.session = Session(LOGIN, PASSWORD)

    # def test_upload(self):
    #     with patch("builtins.open", mock_open(read_data="data")) as mock_file:
    #         assert open("path/to/open").read() == "data"
    #         mock_file.assert_called_with("path/to/open")
    #     filespot = self.session.filespot()
    #     filespot.upload(LOCAL_PATH, PC_PATH)


unittest.main()
