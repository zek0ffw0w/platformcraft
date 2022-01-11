from .logger import logger
from .exceptions import *

import json

FILESPOT_ADDR = "https://filespot.platformcraft.ru/2/fs/container/"


class Filespot():
    def __init__(self, Session):
        self.session = Session

    def upload(self, local_path, pc_path, is_dir):
        logger.debug("filespot.upload: %s as: %s", local_path, pc_path)

        pc_path = self._del_slash(pc_path)
        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path

        # bad request???
        if is_dir:
            response = self.session.post(url + '/')
        else:
            try:
                f = open(local_path, 'rb')
            except Exception as e:
                raise ExceptionOpenFile("cant open file: {}".format(e)) from None

            with f:
                response = self.session.post(url, files={'file': f})
                print(response.text)

    def remove(self, pc_path):
        logger.debug("filespot.remove: %s", pc_path)

        pc_path = self._del_slash(pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path

        response = self.session.delete(url)

    def change(self, pc_path, params):
        logger.debug("filespot.change: %s", pc_path)

        pc_path = self._del_slash(pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path

        body = json.dumps(params)

        response = self.session.put(url, data=body)
        return response

    def file_info(self, pc_path):
        logger.debug("filespot.file_info: %s", pc_path)

        pc_path = self._del_slash(pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path

        response = self.session.get(url)
        return response

    def _del_slash(self, path):
        if path[0] == "/":
            path = path[1:]
        return path
