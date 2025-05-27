from flask import jsonify, make_response
from src.utils.exceptions import CustomAPIException
from src.utils.sucess import SuccessAPIResponse
from src.usecases.users.login_user_usecase import LoginUserUseCase
from src.infraestructure.database.engine import get_db
from src.usecases.users.register_user_usecase import RegisterUserUseCase

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
        result = use_case.execute(data.get('user_name_email'), data.get('password'))
        
        response_body = SuccessAPIResponse("Usuário autenticado com sucesso!", result).to_dict()

        response = make_response(jsonify(response_body))
        
        token = result.get("token")
        if not token:
            raise CustomAPIException("Token não gerado.", 500)

        response.set_cookie(
            key='auth_token',
            value=str(token),
            httponly=True,
            secure=False,  # mudar para True em produção com HTTPS
            samesite='Lax',
            max_age=3600
        )

        return response
            
    except CustomAPIException as e:
            return e.to_dict(), e.status_code
        