from flask import Blueprint, render_template, request, redirect, url_for
from src.api_main.infraestructure.handler.jwt_handler import validate_token
from src.api_main.utils.login_required_util import login_required


frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/home')
def home():
    return render_template('pages/login.html')

@frontend_bp.route('/logout')
def logout():
    response = redirect(url_for('frontend.home'))
    response.set_cookie('auth_token', '', max_age=0)
    return response

@frontend_bp.route('/register')
def register():
    return render_template('pages/register.html')

@frontend_bp.route('/example')
@login_required
def example():
    return render_template('pages/example.html')
