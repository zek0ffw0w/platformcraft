from .auth import Auth
from .filespot import Filespot
from .exceptions import *
from .logger import *

import requests



class Session:
    def __init__(self, login, password):
        self.auth = Auth(login, password)

    def refresh(self):
        self.auth.refresh()

    def filespot(self):
        return Filespot(self)

    @property
    def token(self):
        return self.auth.access_token

    @property
    def owner_id(self):
        return self.auth.owner_id

    def post(self, url, **params):
        params = self._set_auth_header(**params)

        try:
            resp = requests.post(url, **params)
        except Exception as e:
            raise ExceptionHTTPError("http post: {}".format(e)) from None

        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionServerError("unexpected response status: ", self._get_msg_http_error_resp(resp))

    def get(self, url, **params):
        params = self._set_get_header(**params)

        try:
            resp = requests.get(url, **params)
            if resp.ok:
                logger.debug(resp.text)
        except Exception as e:
            raise ExceptionHTTPError("http get error: {}".format(e)) from None

        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionServerError("unexpected response status: ", self._get_msg_http_error_resp(resp))

    def put(self, url, **params):
        params = self._set_change_header(**params)
        try:
            resp = requests.put(url, **params)
        except Exception as e:
            raise ExceptionHTTPError("http put error: {}".format(e)) from None

        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionServerError("unexpected response status: ", self._get_msg_http_error_resp(resp))

    def delete(self, url, **params):
        params = self._set_auth_header(**params)

        try:
            resp = requests.delete(url, **params)
        except Exception as e:
            raise ExceptionHTTPError("http delete error: {}".format(e)) from None

        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionServerError("unexpected response status: ", self._get_msg_http_error_resp(resp))

    def _set_auth_header(self, **params):
        params['headers'] = {'Authorization': 'Bearer ' + self.token}
        return params

    def _set_change_header(self, **params):
        params['headers'] = {'Authorization': 'Bearer ' + self.token, 'Content-Type': 'application/json'}
        return params

    def _get_msg_http_error_resp(self, resp):
        try:
            data = resp.json()
            return data["msg"]
        except:
            return resp.content

    def _set_get_header(self, **params):
        params['headers'] = {'Authorization': 'Bearer ' + self.token}
        return params
