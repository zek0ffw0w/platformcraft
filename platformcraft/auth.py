from .logger import logger
from .exceptions import *
from .model import AuthInfo
from .http import HTTP

import requests
import json


class Auth(HTTP):
    def __init__(self, login, password):
        self.AUTH_ADDR = "https://auth.platformcraft.ru"
        self.token(login, password)

    def token(self, login, password):
        logger.debug("Auth.token %s", login)

        url = self.AUTH_ADDR + '/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {'login': login, 'password': password}

        try:
            resp = requests.post(url, headers=headers, data=body)
            logger.debug("Auth.token requests.post resp.StatusCode: {}".format(resp.status_code))
        except Exception as e:
            raise ExceptionHTTPError("http post: {}".format(e)) from None

        resp = self._handle_resp(resp)
        data = self._get_data(resp)
        return AuthInfo(data)

    def refresh(self):
        logger.debug("Auth.refresh")

        url = self.AUTH_ADDR + '/refresh'
        headers = {'Authorization': 'Bearer ' + self.access_token + ': application/json'}
        body = {'user_id': self.user_id, 'refresh_token': self.refresh_token}

        try:
            resp = requests.post(url, headers=headers, data=json.dumps(body))
            logger.debug("Auth.refresh requests.post resp.StatusCode: {}".format(resp.status_code))
        except Exception as e:
            raise ExceptionHTTPError("http post: {}".format(e)) from None

        resp = self._handle_resp(resp)
        data = self._get_data(resp)
        return AuthInfo(data)

    def _get_data(self, resp):

        try:
            data = resp.json()
            data_json = json.dumps(data)
        except Exception as e:
            raise ExceptionJson("json.dump error {}".format(e)) from None
        else:
            data = json.loads(data_json)

        self.owner_id = data["owner_id"]
        self.access_token = data["access_token"]
        self.user_id = data["user_id"]
        self.refresh_token = data["refresh_token"]

        return data

    def _get_msg_http_error_resp(self, resp):
        try:
            data = resp.json()
            return data["msg"]
        except:
            return resp.content
