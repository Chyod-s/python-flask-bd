from abc import ABC, abstractmethod
from src.api_main.domain.models.users_model import User

class IUserRepository(ABC):
    @abstractmethod
    def get_user(self, user_name: str) -> User | None:
        pass

    @abstractmethod
    def user_exists(self, user_name: str) -> bool:
        pass
