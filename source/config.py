import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'sarthak'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    H_MAIL_SUBJECT_PREFIX = '[Healers At Home]'
    H_MAIL_SENDER = '<noreply@healers.com'
    H_ADMIN = os.environ.get('admin')
    H_POSTS_PER_PAGE = 20
    H_FOLLOWERS_PER_PAGE = 50
    H_COMMENTS_PER_PAGE = 30
    # MAX_SEARCH_RESULTS = 50

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')



config = {
    'default': DevelopmentConfig
}
