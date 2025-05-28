from flask_restx import Api

authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Digite o token JWT no formato: **Bearer <token>**"
    }
}

api = Api(
    title="API Backend-Challenge",
    version="1.0",
    description=(
        "API modelo para futuros projetos utilizando as mesmas tecnologias.\n\n"
        "Acesse o frontend: http://localhost:5055/home"
    ),
    security='jwt',
    authorizations=authorizations
)
