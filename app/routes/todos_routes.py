from flask import Blueprint

todos_bp = Blueprint('todos', __name__)

@todos_bp.route('/')
def list_todos():
    return 'index', 200


@todos_bp.route('/<int:id>')
def show_todo(id):
    return id


@todos_bp.route('/', methods=['POST'])
def create_todo():
    return 'post'


@todos_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update_todo(id):
    return 'PUT/PATCH'


@todos_bp.route('/<int:id>', methods=['POST'])
def delete_todo(id):
    return 'post'
