# HTTP Exceptions
class ExceptionBadRequest(Exception):
    # 400
    pass

class ExceptionForbidden(Exception):
    # 403
    pass

class ExceptionNotFound(Exception):
    # 404
    pass

class ExceptionConflict(Exception):
    # 409
    pass

class ExceptionTooManyRequests(Exception):
    # 429
    pass

class ExceptionInternalServerError(Exception):
    # 500
    pass

class ExceptionHTTPError(Exception):
    # Other http error
    pass








class ExceptionUpload(Exception):
    pass

class ExceptionServerError(Exception):
    pass

class ExceptionOpenFile(Exception):
    pass


class ExceptionJson(Exception):
    pass


class ExceptionAuth(Exception):
    pass


class ExceptionRemove(Exception):
    pass


class ExceptionChange(Exception):
    pass


class ExceptionRefresh(Exception):
    pass


class ExceptionInfo(Exception):
    pass

