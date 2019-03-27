import os
from flask import Flask
from app.config import get_config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

config_name = os.environ.get('APP_ENV')
app.config.from_object(get_config(config_name))
db = SQLAlchemy(app)

from app.routes.tipos_routes import tipos_bp
from app.routes.todos_routes import todos_bp

app.register_blueprint(tipos_bp, url_prefix='/tipos')
app.register_blueprint(todos_bp, url_prefix='/')