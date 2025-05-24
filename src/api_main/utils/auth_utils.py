from werkzeug.security import check_password_hash

def check_password(stored_password_hash: str, password: str) -> bool:
    return check_password_hash(stored_password_hash, password)
