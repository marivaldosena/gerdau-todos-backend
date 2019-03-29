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
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


from app.routes.tipos_routes import tipos_bp
from app.routes.todos_routes import todos_bp

app.register_blueprint(tipos_bp, url_prefix='/tipos')
app.register_blueprint(todos_bp, url_prefix='/')
app.register_blueprint(todos_bp, url_prefix='/todos')
