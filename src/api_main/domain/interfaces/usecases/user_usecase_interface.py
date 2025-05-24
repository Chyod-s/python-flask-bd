from abc import ABC, abstractmethod
from typing import Any

class IUserUseCase(ABC):
    @abstractmethod
    def login (self, username: str, password: str) -> Any:
        pass
    
    @abstractmethod
    def register (self, username: str, password: str) -> Any:
        pass