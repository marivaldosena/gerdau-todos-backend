from flask import Flask

app = Flask(__name__)


@app.route('/')
def list_todos():
    return 'index', 200


@app.route('/<int:id>')
def show_todo(id):
    return id

