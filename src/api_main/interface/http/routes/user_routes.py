from flask_restx import Namespace, Resource
from src.api_main.interface.http.swagger import create_user_parser, login_user_parser
from src.api_main.interface.http.controllers.user_controller import create_user, get_user
from flask_jwt_extended import jwt_required

user_ns = Namespace('backend-challenge', description='API features for users')

@user_ns.route('/login')
@user_ns.expect(login_user_parser)
class LoginUserResource(Resource):
    def post(self):
        args = login_user_parser.parse_args()
        response = get_user(args)
        return response

@user_ns.route('/register')
class CreateUserResource(Resource):
    @user_ns.expect(create_user_parser)
    def post(self):
        args = create_user_parser.parse_args()
        response, status_code = create_user(args)
        return response, status_code

    