from .logger import logger
from .exceptions import *

import json

FILESPOT_ADDR = "https://filespot.platformcraft.ru/2/fs/container/"


class Filespot:
    def __init__(self, Session):
        self.session = Session

    def upload(self, local_path, pc_path):
        logger.debug("filespot.upload: %s as: %s", local_path, pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path

        try:
            f = open(local_path, 'rb')
        except Exception as e:
            raise ExceptionOpenFile("cant open file: {}".format(e)) from None

        with f:
            self.session.post(url, files={'file': f})

    def remove(self, pc_path):
        logger.debug("filespot.remove: %s", pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path

        self.session.delete(url)

    def change(self, pc_path, params):
        logger.debug("filespot.change: %s", pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path

        body = json.dumps(params)

        self.session.put(url, data=body)

    def file_info(self, pc_path):
        logger.debug("filespot.file_info: %s", pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path  # Укажите свой {owner_ID} и путь к файлу {path_file} после "/object/"

        self.session.get(url)
