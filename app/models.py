from app import db, ma
from flask_marshmallow.fields import fields


class Todo(db.Model):
    """
    Armazena detalhes da tarefa criada.

    As informações armazenas são nome da tarefa, tipo, e data de entrega.

    """
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(120), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    finalizado = db.Column(db.Boolean, default=False)
    data_entrega = db.Column(db.DateTime)

    def __str__(self):
        return '<Todo: {}>'.format(self.todo)

    def __repr__(self):
        return '<Todo: {}>'.format(self.todo)


class TodoSchema(ma.Schema):
    data_entrega = fields.DateTime(dump_to='dataEntrega')
    
    class Meta:
        fields = ('id', 'todo', 'tipo', 'finalizado', 'data_entrega')
        
