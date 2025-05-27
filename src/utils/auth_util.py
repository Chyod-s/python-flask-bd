from werkzeug.security import check_password_hash

def check_password(stored_password_hash: str, password: str) -> bool:
    return check_password_hash(stored_password_hash, password)

def check_email(email: str) -> bool:
    if not email or "@" not in email or "." not in email:
        return False
    return True