class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = '045ef2d78b754b07d19b8b5e64971582'

    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "badrhymes@yandex.ru"
    MAIL_PASSWORD = "Ybrjkfif1"