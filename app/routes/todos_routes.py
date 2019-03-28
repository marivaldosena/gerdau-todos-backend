import datetime
from flask import Blueprint, request, jsonify

todos_bp = Blueprint('todos', __name__)

from app.models import Todo, TodoSchema, db


@todos_bp.route('/')
def list():
    resultado = Todo.query.all()
    schema = TodoSchema(many=True)

    return schema.jsonify(resultado), 200


@todos_bp.route('/<int:id>')
def show(id):
    todo = Todo.query.get_or_404(id)

    schema = TodoSchema()

    return schema.jsonify(todo), 200


@todos_bp.route('/', methods=['POST'])
def create():
    schema = TodoSchema()

    json = request.get_json()
    d = schema.load(json).data

    todo = Todo(todo=d['todo'],
                tipo_id=d['tipo_id'],
                finalizado=d['finalizado'],
                data_entrega=datetime.datetime.fromisoformat(d['data_entrega']))

    db.session.add(todo)
    db.session.commit()

    return schema.jsonify(todo), 201


@todos_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id):
    schema = TodoSchema()

    json = request.get_json()
    d = schema.load(json).data

    todo = Todo.query.get_or_404(id)

    todo.todo = d['todo']
    todo.tipo_id = d['tipo_id']
    todo.finalizado = d['finalizado']
    todo.data_entrega = datetime.datetime.fromisoformat(d['data_entrega'])

    db.session.add(todo)
    db.session.commit()

    return schema.jsonify(todo), 200



@todos_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    todo = Todo.query.get_or_404(id)

    db.session.delete(todo)
    db.session.commit()

    return jsonify({'status': 'Item excluído'}), 204
