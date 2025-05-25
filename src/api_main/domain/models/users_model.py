from src.api_main.utils.exceptions import CustomAPIException
from src.api_main.domain.models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModel):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    confirm_password = Column(String, nullable=False)
    name = Column(String, nullable=True)

    def __init__(self, user_name: str, email: str, password: str, confirm_password: str, name: str | None):
        self.user_name = user_name
        self.email = email
        self.password = generate_password_hash(password)
        self.confirm_password = generate_password_hash(confirm_password)
        self.name = name
    
    @classmethod
    def get_user(cls, db, user_name: str | None = None, email: str | None = None):
        try:
            if not user_name and not email:
                raise CustomAPIException("Informe um: usuário ou e-mail.", 422)

            if user_name:
                user = db.query(cls).filter_by(user_name=user_name).first()
            else:
                user = db.query(cls).filter_by(email=email).first()

            return user

        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None


    @classmethod
    def check_password(cls, stored_password: str, password: str):
        return check_password_hash(stored_password, password)
    
    @classmethod
    def user_exists(cls, db, user_name: str):
        return db.query(cls).filter_by(user_name=user_name).first() is not None