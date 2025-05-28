import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../migrations/data'))
os.makedirs(BASE_DIR, exist_ok=True)

DB_PATH = os.path.join(BASE_DIR, 'app.db')
DATABASE_URL = f"sqlite:///{DB_PATH}"
