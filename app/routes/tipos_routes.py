from flask import Blueprint

tipos_bp = Blueprint('tipos', __name__)

from app.models import Tipo


@tipos_bp.route('/')
def list():
    resultado = Tipo.query.all()
    return resultado, 200


@tipos_bp.route('/<int:id>')
def show(id):
    return id, 200


@tipos_bp.route('/', methods=['POST'])
def create():
    return 'post', 201


@tipos_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id):
    return 'PUT/PATCH',


@tipos_bp.route('/<int:id>', methods=['POST'])
def delete(id):
    return 'post', 204
