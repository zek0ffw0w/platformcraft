import platformcraft
import logging
import logging.config

LOGIN = "zek0ffw0w"
PASSWORD = "123456"

LOCAL_PATH = "C:/Users/malyc/Downloads/wiegand-produkte_en_1-710x368.mp4"
PC_PATH = "vidik"
info_test = "file_info_test"
test_t = "upltest1"
params = {'name': "file_info_test", 'description': "test description", 'private': False}


def main():
    try:
        session = platformcraft.Session(LOGIN, PASSWORD)
    except Exception as e:
        logging.error("unsuccessful login: %s", e)
        return

    filespot = session.filespot()

    try:
        object = filespot.upload(LOCAL_PATH, PC_PATH)
    except Exception as e:
        logging.error("unsuccessful upload: %s", e)
        return

    try:
        object = filespot.remove(PC_PATH)
    except Exception as e:
        logging.error("unsuccessful remove: %s", e)
        return

    try:
        object = filespot.file_info(info_test)
    except Exception as e:
        logging.error("unsuccessful getting info: %s", e)
        return

    try:
        object = filespot.change(info_test, params)
    except Exception as e:
        logging.error("unsuccessful changing: %s", e)
        return

    try:
        session = session.refresh()
    except Exception as e:
        logging.error("unsuccessful refresh: %s", e)
        return


if __name__ == '__main__':
    DEFAULT_LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '{asctime} {levelname}:{module}:{message}',
                'style': '{',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
            },
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
            },
            'platformcraft': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
        }
    }
    logging.config.dictConfig(DEFAULT_LOGGING)

    main()
