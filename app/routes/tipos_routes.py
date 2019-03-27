from flask import Blueprint

tipos_bp = Blueprint('tipos', __name__)

from app.main import db
from app.models import Tipo

@tipos_bp.route('/')
def list():
    lista = Tipo.query.all()

    return lista