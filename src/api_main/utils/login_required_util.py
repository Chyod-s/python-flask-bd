from functools import wraps
from flask import request, redirect, url_for
from src.api_main.infraestructure.handler.jwt_handler import validate_token

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('auth_token')
        if not token or not validate_token(token):
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated
