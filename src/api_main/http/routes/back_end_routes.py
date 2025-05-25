from flask_restx import Namespace, Resource
from src.api_main.http.swagger_parse import register_user_parser, login_user_parser
from src.api_main.http.controllers.user_controller import register_user, login_user
from src.api_main.http.swagger_config import api
from src.api_main.http.swagger_models import register_models
from flask_jwt_extended import jwt_required

user_ns = Namespace('backend-challenge', description='API features for users')
success_model, error_model = register_models(api)

@user_ns.route('/register')
@user_ns.response(201, 'Usuário criado com sucesso', success_model)
@user_ns.response(400, 'Requisição inválida', error_model)
@user_ns.response(422, 'Erro de validação', error_model)
@user_ns.response(500, 'Erro interno do servidor', error_model)
class CreateUserResource(Resource):
    @user_ns.expect(register_user_parser)
    def post(self):
        args = register_user_parser.parse_args()
        response, status_code = register_user(args)
        return response, status_code

@user_ns.route('/login')
@user_ns.expect(login_user_parser)
@user_ns.response(200, 'Login realizado com sucesso', success_model)
@user_ns.response(400, 'Requisição inválida', error_model)
@user_ns.response(401, 'Não autorizado', error_model)
class LoginUserResource(Resource):
    def post(self):
        args = login_user_parser.parse_args()
        response = login_user(args)
        return response

api.add_namespace(user_ns, path="/api")