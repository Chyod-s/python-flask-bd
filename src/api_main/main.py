import sys
import os
from src.api_main.infraestructure.scheduler.task_scheduler import start_scheduler
from flask import Flask
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from src.api_main.infraestructure.database import init_db, engine
from src.api_main.config import Config
from src.api_main.http.swagger_config import api
from flask_cors import CORS
from src.api_main.http.routes.front_end_routes import frontend_bp
from src.api_main.http.routes import back_end_routes

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

scheduler = start_scheduler()

load_dotenv()

secret_key = os.getenv("SECRET_KEY")

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

app.config.from_object(Config)
Config.validate()

CORS(app=app,
    CORS_SUPPORTS_CREDENTIALS=app.config['CORS_SUPPORTS_CREDENTIALS'],
    resources=app.config['CORS_RESOURCES'])

app.secret_key = secret_key

app.config.from_object(Config)

api.init_app(app)

jwt = JWTManager(app)

app.register_blueprint(frontend_bp)

init_db(engine)

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
