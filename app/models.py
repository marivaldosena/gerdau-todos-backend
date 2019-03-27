from .main import db


class Tipo(db.Model):
    __tablename__ = 'tipos'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), null=False)
    todos = db.relationship('Todo', backref='tipo')


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(50), null=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipos.id'), null=False)
