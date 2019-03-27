from flask import Blueprint

tipos_bp = Blueprint('tipos', __name__)

@tipos_bp.route('/')
def list():
    return 'tipos'