import os
from flask import Flask
from .config import get_config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

config_name = os.environ.get('APP_ENV')
app.config.from_object(get_config(config_name))
db = SQLAlchemy(app)


@app.route('/')
def list_todos():
    return 'index', 200


@app.route('/<int:id>')
def show_todo(id):
    return id
