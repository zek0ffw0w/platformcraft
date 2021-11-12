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
            response = self.session.post(url, files={'file': f})
            return response

    def remove(self, pc_path):
        logger.debug("filespot.remove: %s", pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path

        response = self.session.delete(url)
        if response.ok:
            return response

    def change(self, pc_path, params):
        logger.debug("filespot.change: %s", pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path

        body = json.dumps(params)

        response = self.session.put(url, data=body)
        if response.ok:
            return response

    def file_info(self, pc_path):
        logger.debug("filespot.file_info: %s", pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path  # Укажите свой {owner_ID} и путь к файлу {path_file} после "/object/"

        response = self.session.get(url)
        return response
