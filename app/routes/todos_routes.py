from flask import Blueprint

todos_bp = Blueprint('todos', __name__)


@todos_bp.route('/')
def list():
    return 'index', 200


@todos_bp.route('/<int:id>')
def show(id):
    return id


@todos_bp.route('/', methods=['POST'])
def create():
    return 'post'


@todos_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id):
    return 'PUT/PATCH'


@todos_bp.route('/<int:id>', methods=['POST'])
def delete(id):
    return 'post'
