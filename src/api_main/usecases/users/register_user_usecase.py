from src.api_main.infraestructure.handler.jwt_handler import generate_token
from src.api_main.utils.exceptions import CustomAPIException
from src.api_main.domain.models.users_model import User
from flask_jwt_extended import get_csrf_token

class RegisterUserUseCase:
    def __init__(self, db):
        self.db = db

    def execute(self, user_name: str, email: str, password: str, confirm_password: str, name: str | None):
        if not user_name or not password:
            raise CustomAPIException("Informe um nome de usuário e uma senha válidos.", 422)

        if User.user_exists(self.db, user_name):
            raise CustomAPIException("Usuário já existe.", 422)
        
        if password != confirm_password:
            raise CustomAPIException("As senhas não coincidem.", 422)

        new_user = User(user_name=user_name, email=email, password=password, confirm_password=confirm_password, name=name)

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        token = generate_token(user_id=new_user.id) # type: ignore
        csrf_token = get_csrf_token(token)
        
        return {
            "token": token,
            "csrf_token": csrf_token,
            "user_id": new_user.id
            }
