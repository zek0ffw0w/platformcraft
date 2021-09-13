from logger import logger
import requests
import json


from exceptions import *

AUTH_ADDR = "https://auth.platformcraft.ru"


class Auth:
    def __init__(self, login, password):
        self.token(login, password)

    def token(self, login, password):
        logger.debug("login in to %s", AUTH_ADDR)
        url = AUTH_ADDR + '/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {'login': login, 'password': password}
        try:
            resp = requests.post(url, headers=headers, data=body)
            if resp.ok:
                print(resp.status_code)
                print(resp.text)
                self.get_data(resp)
                return resp
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionAuth(self._get_msg_http_error_resp(resp))

    def _get_msg_http_error_resp(self, resp):
        try:
            data = resp.json()
            return data["msg"]
        except:
            return resp.content

    def refresh(self):
        logger.debug("refreshing token to %s", AUTH_ADDR)
        url = AUTH_ADDR + '/refresh'
        headers = {'Authorization': 'Bearer ' + self.access_token + ': application/json'}
        body = {'user_id': self.user_id, 'refresh_token': self.refresh_token}
        try:
            resp = requests.post(url, headers=headers, data=json.dumps(body))
            if resp.ok:
                print(resp.status_code)
                print(resp.text)
                self.get_data(resp)
                return resp
        except requests.ConnectionError:
            raise ConnectionError(self._get_msg_http_error_resp(resp))
        try:
            resp.raise_for_status()
        except Exception:
            raise ExceptionRefresh(self._get_msg_http_error_resp(resp))

        self.get_data(resp)

    def get_data(self, resp):

        data = resp.json()
        data_json = json.dumps(data)
        data = json.loads(data_json)

        self.owner_id = data["owner_id"]
        self.access_token = data["access_token"]
        self.user_id = data["user_id"]
        self.refresh_token = data["refresh_token"]
