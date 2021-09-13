from auth import Auth
from filespot import Filespot
from exceptions import *
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
        params = self.set_auth_header(**params)
        try:
            resp = requests.post(url, **params)
            if resp.ok:
                return resp
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionUpload(self._get_msg_http_error_resp(resp))
        finally:
            print(resp.status_code)
            print(resp.headers)
            print(resp.text)

    def get(self, url, **params):
        params = self._set_get_header(**params)
        try:
            resp = requests.get(url, **params)
            if resp.ok:
                return resp
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionInfo(self._get_msg_http_error_resp(resp))

    def put(self, url, **params):
        params = self._set_change_header(**params)
        try:
            resp = requests.put(url, **params)
            print(resp)
            if resp.ok:
                return resp
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionChange(self._get_msg_http_error_resp(resp))

    def delete(self, url, **params):
        params = self.set_auth_header(**params)
        try:
            resp = requests.delete(url, **params)
            if resp.ok:
                return resp
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionRemove(self._get_msg_http_error_resp(resp))

    def set_auth_header(self, **params):
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
