from flask_restx import reqparse

register_user_parser = reqparse.RequestParser()
register_user_parser.add_argument('user_name', type=str, required=True, location='json', help='Nome do usuário')
register_user_parser.add_argument('password', type=str, required=True, location='json', help='Senha do usuário')
