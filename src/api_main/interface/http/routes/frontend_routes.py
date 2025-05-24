from flask import Blueprint, render_template, request, redirect, url_for
from src.api_main.utils.login_required_util import login_required
from src.api_main.utils.auth_utils import validate_jwt_token

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/home')
def home():
    token = request.cookies.get('auth_token')
    print(f"Token recebido no /home: {token}")
    
    if token and validate_jwt_token(token):
        print("Token válido, redirecionando para dashboard")
        return redirect(url_for('frontend.dashboard'))
    
    print("Token inválido ou não encontrado, redirecionando para login")
    return render_template('pages/login.html')

@frontend_bp.route('/logout')
def logout():
    response = redirect(url_for('frontend.home'))
    response.set_cookie('auth_token', '', max_age=0)
    return response

@frontend_bp.route('/register')
def register():
    return render_template('pages/register.html')
