
class Config:
    SECRET_KEY = 'e04ebe24c3e81cc08f6474ff5ab26624'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # 'MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # 'MAIL_PASSWORD = os.environ.get('PASSWORD')

    MAIL_USERNAME = 'ishan.dhaliwal@gmail.com'
    MAIL_PASSWORD = 'GurgaoN19'