from .auth import Auth
from .filespot import Filespot
from .http import HTTP


class Session(HTTP):
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
