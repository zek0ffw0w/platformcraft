from .logger import logger
from .exceptions import *
from .model import UploadInfo

import json

FILESPOT_ADDR = "https://filespot.platformcraft.ru/2/fs/container/"


class Filespot():
    def __init__(self, Session):
        self.session = Session

    def upload(self, local_path, pc_path, is_dir):
        logger.debug("filespot.upload: %s as: %s", local_path, pc_path)

        pc_path = self._del_slash(pc_path)
        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path
        tr = True
        body = {'name': pc_path, 'is_dir': tr, 'type': ''}
        body = json.dumps(body)
        # bad request???
        if is_dir:
            response = self.session.post(url, data=body)
        else:
            try:
                f = open(local_path, 'rb')
            except Exception as e:
                raise ExceptionOpenFile("cant open file: {}".format(e)) from None

            with f:
                response = self.session.post(url, files={'file': f})

        data = self._get_data(response)
        print(data["id"])
        return UploadInfo(data)

    def remove(self, pc_path):
        logger.debug("filespot.remove: %s", pc_path)

        pc_path = self._del_slash(pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path

        response = self.session.delete(url)

    def change(self, pc_path, name=None, dir=None, description=None, private=False, max_height=None, max_width=None):
        logger.debug("filespot.change: %s", pc_path)

        pc_path = self._del_slash(pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path

        params = {'name': name, 'description': description, 'dir': dir, 'private': private, 'max_height': max_height, 'max_width': max_width}

        body = json.dumps(params)

        response = self.session.put(url, data=body)
        return response

    def file_info(self, pc_path):
        logger.debug("filespot.file_info: %s", pc_path)

        pc_path = self._del_slash(pc_path)

        url = FILESPOT_ADDR + self.session.owner_id + '/object/' + pc_path

        response = self.session.get(url)
        print(response.text)
        return response

    def _del_slash(self, path):
        if path[0] == "/":
            path = path[1:]
        return path

    def _get_data(self, resp):

        try:
            data = resp.json()
            data_json = json.dumps(data)
        except Exception as e:
            raise ExceptionJson("json.dump error {}".format(e)) from None
        else:
            data = json.loads(data_json)

        self.id = data["id"]
        self.is_dir = data["is_dir"]
        self.type = data["type"]
        self.status = data["status"]
        self.name = data["name"]
        self.path = ["path"]
        self.size = data["size"]
        self.content_type = data["content_type"]
        self.description = data["description"]
        self.create_time = ["create_time"]
        self.change_time = data["change_time"]
        self.create_time = data["create_date"]
        self.latest_update = ["latest_update"]
        self.private = data["private"]

        return data
