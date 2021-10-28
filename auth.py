from .logger import logger
from .exceptions import *

from http import HTTPStatus
import requests
import json


class Auth:
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

        else:
            if resp.ok:
                self._get_data(resp)
                return resp
            if resp.status_code == HTTPStatus.FORBIDDEN:
                raise ExceptionAuth("login or password incorrect")
            if resp.status_code == HTTPStatus.BAD_REQUEST:
                raise ExceptionBadRequest("Bad request")
            if resp.status_code == HTTPStatus.NOT_FOUND:
                raise ExceptionNotFound("Not found")
            if resp.status_code == HTTPStatus.CONFLICT:
                raise ExceptionConflict("Conflicting request")
            if resp.status_code == HTTPStatus.TOO_MANY_REQUESTS:
                raise ExceptionTooManyRequests("Too many requests")
            if resp.status_code > 500:
                raise ExceptionInternalServerError("Something went wrong, internal server error")


        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionServerError("unexpected response status: {}".format(resp.status_code)) from None

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

        else:
            if resp.ok:
                self._get_data(resp)
                return resp
            if resp.status_code == HTTPStatus.FORBIDDEN:
                raise ExceptionRefresh("user id or access token or refresh token incorrect")
            if resp.status_code == HTTPStatus.BAD_REQUEST:
                raise ExceptionBadRequest("Bad request")
            if resp.status_code == HTTPStatus.NOT_FOUND:
                raise ExceptionNotFound("Not found")
            if resp.status_code == HTTPStatus.CONFLICT:
                raise ExceptionConflict("Conflicting request")
            if resp.status_code == HTTPStatus.TOO_MANY_REQUESTS:
                raise ExceptionTooManyRequests("Too many requests")
            if resp.status_code > 500:
                raise ExceptionInternalServerError("Something went wrong, internal server error")

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
