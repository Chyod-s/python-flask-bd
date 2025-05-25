import jwt
from src.api_main.config import Config

def extract_csrf_token(token: str):
    try:
        payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
        return payload.get('csrf')
    except Exception:
        return None
