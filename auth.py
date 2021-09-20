from .logger import logger
from .exceptions import *

from http import HTTPStatus
import requests
import json

AUTH_ADDR = "https://auth.platformcraft.ru"


class Auth:
    def __init__(self, login, password):
        self.token(login, password)

    def token(self, login, password):
        logger.debug("Auth.token %s", login)

        url = AUTH_ADDR + '/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {'login': login, 'password': password}

        try:
            resp = requests.post(url, headers=headers, data=body)
            logger.debug("Auth.token requests.post resp.StatusCode: {}".format(resp.status_code))
        except Exception as e:
            raise ExceptionHTTPError("http post: {}".format(e)) from None

        else:
            if resp.ok:
                self._get_data(resp)
            if resp.status_code == HTTPStatus.FORBIDDEN:
                raise ExceptionAuth("login or password incorrect")

        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionServerError("unexpected response status: {}".format(resp.status_code)) from None

    def refresh(self):
        logger.debug("refreshing token")

        url = AUTH_ADDR + '/refresh'
        headers = {'Authorization': 'Bearer ' + self.access_token + ': application/json'}
        body = {'user_id': self.user_id, 'refresh_token': self.refresh_token}

        try:
            resp = requests.post(url, headers=headers, data=json.dumps(body))
            logger.debug("Auth.refresh requests.post resp.StatusCode: {}".format(resp.status_code))
        except Exception as e:
            raise ExceptionHTTPError("http post: {}".format(e)) from None

        else:
            if resp.ok:
                self._get_data(resp)
            if resp.status_code == HTTPStatus.FORBIDDEN:
                raise ExceptionRefresh("user id or access token or refresh token incorrect")
            if resp.status_code == HTTPStatus.UNAUTHORIZED:
                raise ExceptionAuth("Unauthorized")

        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionServerError("unexpected response status: {}".format(resp.status_code)) from None

        self._get_data(resp)

    def _get_data(self, resp):
        try:
            data = resp.json()
        except Exception as e:
            raise ExceptionJson("cant get json from response {}".format(e)) from None
        else:

            try:
                data_json = json.dumps(data)
            except Exception as e:
                raise ExceptionJson("json.dump error {}".format(e)) from None
            else:
                data = json.loads(data_json)

        self.owner_id = data["owner_id"]
        self.access_token = data["access_token"]
        self.user_id = data["user_id"]
        self.refresh_token = data["refresh_token"]

    def _get_msg_http_error_resp(self, resp):
        try:
            data = resp.json()
            return data["msg"]
        except:
            return resp.content
