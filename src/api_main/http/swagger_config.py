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
    title="API Precatory Creditor",
    version="1.0",
    description = (
        "API para gestão de credores e documentos precatórios, incluindo cadastro, autenticação e emissão de certificados.\n"
        "\n"
        "Acesse o frontend: http://localhost:5055/home"
    ),
    contact_email="hix_x@hotmail.com",
    license="MIT",
    license_url="https://opensource.org/licenses/MIT",
    authorizations=authorizations,
    security='jwt'
)
