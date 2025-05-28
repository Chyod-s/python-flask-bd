import os

class BaseConfig:
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 5055

    JWT_SECRET_KEY = os.getenv('JWT_SECRET')
    JWT_ALGORITHM = 'HS256'
    JWT_EXP_DELTA_SECONDS = 3600
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'

    ALLOWED_EXTENSIONS = {'docx', 'doc', '.jpg', '.jpeg', '.png', '.pdf'}
    MAX_FILE_SIZE = 5 * 1024 * 1024

    CORS_SUPPORTS_CREDENTIALS = True
    CORS_RESOURCES = {
        r"/*": {"origins": os.getenv('CORS_ORIGIN', 'http://localhost:5055')}
    }

    @staticmethod
    def validate():
        if not os.getenv('JWT_SECRET'):
            raise ValueError("JWT_SECRET environment variable not set")
