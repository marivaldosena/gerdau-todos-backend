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

    nome = request.json['todo']
    tipo = request.json['tipo']
    finalizado = request.json.get('finalizado') or False
    data_entrega = request.json['dataEntrega']

    todo = Todo(todo=nome,
                tipo=tipo,
                finalizado=finalizado)

    if str(data_entrega).isnumeric:
        todo.data_entrega=datetime.datetime.now()
    else:
        todo.data_entrega=datetime.date.fromisoformat(data_entrega)

    db.session.add(todo)
    db.session.commit()

    return schema.jsonify(todo), 201


@todos_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id):
    schema = TodoSchema()

    nome = request.json['todo']
    tipo = request.json['tipo']
    finalizado = request.json.get('finalizado') or False
    data_entrega = request.json['dataEntrega']

    todo = Todo.query.get_or_404(id)

    todo.todo = nome
    todo.tipo = tipo
    todo.finalizado = finalizado

    if str(data_entrega).isnumeric:
        todo.data_entrega=datetime.datetime.now()
    else:
        todo.data_entrega=datetime.date.fromisoformat(data_entrega)

    db.session.add(todo)
    db.session.commit()

    return schema.jsonify(todo), 200



@todos_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    todo = Todo.query.get_or_404(id)

    db.session.delete(todo)
    db.session.commit()

    return jsonify({'status': 'Item excluído'}), 204
