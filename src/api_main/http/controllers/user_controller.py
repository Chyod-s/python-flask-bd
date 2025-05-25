from src.api_main.utils.exceptions import CustomAPIException
from src.api_main.utils.sucess import SuccessAPIResponse
from src.api_main.usecases.users.login_user_usecase import LoginUserUseCase
from src.api_main.infraestructure.database.engine import get_db
from src.api_main.usecases.users.register_user_usecase import RegisterUserUseCase

def register_user(data):
    db = next(get_db())
    try:
        use_case = RegisterUserUseCase(db)
        result = use_case.execute(data.get('user_name'), data.get('email') , data.get('password'), data.get('confirm_password'), data.get('name'))

        response = SuccessAPIResponse("Usuário criado com sucesso!", result, 201)
        
        return response.to_dict(), response.status_code
    
    except CustomAPIException as e:
        return e.to_dict(), e.status_code

def login_user(data):
    db = next(get_db())

    try:
        use_case = LoginUserUseCase(db)
        result = use_case.execute(data.get('user_name'), data.get('password'))
        
        response = SuccessAPIResponse("Usuário autenticado com sucesso!", result)

        return response.to_dict(), response.status_code
            
    except CustomAPIException as e:
            return e.to_dict(), e.status_code
        