class AuthInfo:
    def __init__(self, data):
        self.user_id = data["user_id"]
        self.owner_id = data["owner_id"]
        self.expires_at = data["expires_at"]