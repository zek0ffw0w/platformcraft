from logger import *
from exceptions import *
import json

FILESPOT_ADDR = "https://filespot.platformcraft.ru/2/fs/container/"


class Filespot:
    def __init__(self, Session):
        self.session = Session

    def upload(self, local_path, pc_path):
        logger.debug("upload from %s to %s", local_path, pc_path)
        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path
        try:
            files = {'file': open(local_path, 'rb')}
        except Exception as e:
            raise ExceptionUpload("open file {}".format(e))
        try:
            self.session.post(url, files=files)
        except Exception as e:
            raise ExceptionUpload("cant upload file {}".format(e))

    def remove(self, pc_path):
        logger.debug("removing %s", pc_path)
        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path
        try:
            self.session.delete(url)
        except Exception as e:
            raise ExceptionRemove("cant delete file {}".format(e))

    def change(self, pc_path, params):
        logger.debug("changing %s", pc_path)
        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path
        body = json.dumps(params)
        try:
            self.session.put(url, data=body)
        except Exception as e:
            raise ExceptionChange("cant change, file {}".format(e))

    def file_info(self, pc_path):
        logger.debug("getting info from %s", pc_path)
        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path  # Укажите свой {owner_ID} и путь к файлу {path_file} после "/object/"

        try:
            self.session.get(url)
        except Exception as e:
            raise ExceptionInfo("cant get file info {}".format(e))