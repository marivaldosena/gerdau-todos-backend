from flask import Blueprint, jsonify, request

tipos_bp = Blueprint('tipos', __name__)

from app.models import Tipo, TipoSchema, db


@tipos_bp.route('/')
def list():
    resultado = Tipo.query.all()
    tipo_schema = TipoSchema(many=True)

    return tipo_schema.jsonify(resultado), 200


@tipos_bp.route('/', methods=['POST'])
def create():
    nome = request.json['tipo']

    tipo = Tipo(tipo=nome)

    db.session.add(tipo)
    db.session.commit()

    tipo_schema = TipoSchema()

    return tipo_schema.jsonify(tipo), 201


@tipos_bp.route('/<int:id>', methods=['GET'])
def show(id):
    resultado = Tipo.query.get_or_404(id)
    tipo_schema = TipoSchema()

    return tipo_schema.jsonify(resultado), 200


@tipos_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    tipo = Tipo.query.get_or_404(id)

    db.session.delete(tipo)
    db.session.commit()
    return jsonify({'status': 'Item excluído'}), 204


@tipos_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id):
    nome = request.json['tipo']

    tipo = Tipo.query.get_or_404(id)
    tipo.tipo = nome

    db.session.delete(tipo)
    db.session.commit()

    schema = TipoSchema()

    return schema.jsonify(tipo), 200
