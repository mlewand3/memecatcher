import os

basedir = os.path.abspath(os.path.dirname(__file__))


class LocalConfig(object):
    TESTING = True
    CSRF_ENABLED = True
    USER_APP_NAME = "MEME-Catcher"


class ProductionConfig(object):
    TESTING = False
    CSRF_ENABLED = True
    USER_APP_NAME = "MEME-Catcher"
