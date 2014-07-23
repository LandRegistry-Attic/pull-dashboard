class Config(object):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(DevelopmentConfig):
    DEBUG = True
    TESTING = True
