import uuid
import jwt
from datetime import datetime, timedelta, timezone
from src.api_main.config import Config

config = Config()

SECRET_KEY = config.JWT_SECRET_KEY
ALGORITHM = config.JWT_ALGORITHM
EXP_DELTA_SECONDS = config.JWT_EXP_DELTA_SECONDS

def generate_token(user_id: int):
    now_utc = datetime.now(timezone.utc)
    payload = {
        'sub': str(user_id),
        'iat': int(now_utc.timestamp()),
        'exp': int((now_utc + timedelta(seconds=EXP_DELTA_SECONDS)).timestamp()),
        'jti': str(uuid.uuid4()),
        'type': 'access',
        'nbf': int(now_utc.timestamp()),
        'csrf': str(uuid.uuid4())
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], leeway=10)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise Exception('Token expirado, faça login novamente.')
    except jwt.InvalidTokenError:
        raise Exception('Token inválido, faça login novamente.')


def validate_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError as e:
        print(f"Erro: Token expirado: {e}")
        return None
    except jwt.InvalidTokenError as e:
        print(f"Erro: Token inválido: {e}")
        return None
