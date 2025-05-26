from typing import Any
from src.api_main.utils.auth_util import check_email, check_password
from src.api_main.infraestructure.handler.jwt_handler import generate_token
from src.api_main.utils.exceptions import CustomAPIException
from src.api_main.domain.models.users_model import User
from flask_jwt_extended import get_csrf_token

class LoginUserUseCase():
    def __init__(self, db):
        self.db = db

    def execute(self, user_name_email: str, password: str) -> dict[str, Any]:
        if not user_name_email or not password:
            raise CustomAPIException("Informe um nome de usuário e uma senha válidos.", 422)
        
        if check_email(user_name_email):
            user = User.get_user(self.db, email=user_name_email)
        else:
            user = User.get_user(self.db, user_name=user_name_email)
        
        if not user:
            raise CustomAPIException("Usuário não encontrado.", 422)

        if not check_password(user.password,password):
            raise CustomAPIException("Senha inválida.", 422)

        user_name = "".join(user.name) if user.name is not None else user.user_name
        token = generate_token(user.id) 
        csrf_token = get_csrf_token(token)
        
        User.att_updated_at(self.db, user)
 
        return {
            "user_name": user_name,
            "csrf_token": csrf_token,
            "token": token
        }
