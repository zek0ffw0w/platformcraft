from http import HTTPStatus
import requests

from .exceptions import *


class HTTP:
    def post(self, url, **params):
        params = self._set_auth_header(**params)

        try:
            resp = requests.post(url, **params)
        except Exception as e:
            raise ExceptionHTTPError("http post: {}".format(e)) from None

        return self._handle_resp(resp)

    def get(self, url, **params):
        params = self._set_get_header(**params)

        try:
            resp = requests.get(url, **params)
        except Exception as e:
            raise ExceptionHTTPError("http get error: {}".format(e)) from None

        return self._handle_resp(resp)

    def put(self, url, **params):
        params = self._set_change_header(**params)

        try:
            resp = requests.put(url, **params)
        except Exception as e:
            raise ExceptionHTTPError("http put error: {}".format(e)) from None

        return self._handle_resp(resp)

    def delete(self, url, **params):
        params = self._set_auth_header(**params)

        try:
            resp = requests.delete(url, **params)
        except Exception as e:
            raise ExceptionHTTPError("http delete error: {}".format(e)) from None

        return self._handle_resp(resp)

    def _handle_resp(self, resp):
        if resp.ok:
            return resp
        if resp.status_code == HTTPStatus.BAD_REQUEST:
            raise ExceptionBadRequest("Bad request")
        elif resp.status_code == HTTPStatus.FORBIDDEN:
            raise ExceptionForbidden("login or password incorrect")
        elif resp.status_code == HTTPStatus.NOT_FOUND:
            raise ExceptionNotFound("Not found")
        elif resp.status_code == HTTPStatus.CONFLICT:
            raise ExceptionConflict("Conflicting request")
        elif resp.status_code == HTTPStatus.TOO_MANY_REQUESTS:
            raise ExceptionTooManyRequests("Too many requests")
        elif resp.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
            raise ExceptionInternalServerError("Something went wrong, internal server error")
        else:
            raise ExceptionHTTPError("Unhandled http error. Code: {}".format(resp.status_code)) from None

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
