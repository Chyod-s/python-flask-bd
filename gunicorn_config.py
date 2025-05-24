import os

bind = f"{os.getenv('FLASK_HOST', '0.0.0.0')}:{os.getenv('FLASK_PORT', '5055')}"
workers = int(os.getenv('GUNICORN_WORKERS', '2'))
threads = 2
timeout = 120
loglevel = 'info'
