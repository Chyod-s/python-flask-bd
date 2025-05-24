import os

env = os.getenv('FLASK_ENV', 'development')

if env == 'production':
    from .production import ProductionConfig as Config
else:
    from .development import DevelopmentConfig as Config
