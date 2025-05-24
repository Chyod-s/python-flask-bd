from src.api_main.domain.interfaces.repositories.user_repository_interface import IUserRepository
from src.api_main.domain.models.users_model import User

class UserRepository(IUserRepository):
    def __init__(self, db_session):
        self.db = db_session

    def get_user(self, user_name: str) -> User | None:
        try:
            return self.db.query(User).filter_by(user_name=user_name).first()
        except Exception as e:
            print(f"Error retrieving user: {e}")
            return None

    def user_exists(self, user_name: str) -> bool:
        return self.db.query(User).filter_by(user_name=user_name).first() is not None
