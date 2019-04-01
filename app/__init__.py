import os
from flask import Flask
from app.config import get_config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

config_name = os.environ.get('APP_ENV')
app.config.from_object(get_config(config_name))
db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.after_request
def configurar_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response

from app.routes.todos_routes import todos_bp

app.register_blueprint(todos_bp, url_prefix='/')
app.register_blueprint(todos_bp, url_prefix='/todos')
