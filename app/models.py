from .main import db

class Tipo(db.Model):
    """
    Armazena as informações relacionadas ao tipo de tarefa.

    Os tipos pré-cadastrados são Pessoal e Profissional. No entanto, a plataforma
    permite que os tipos sejam expandidos de acordo com a necessidade.

    """
    __tablename__ = 'tipos'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), null=False)
    todos = db.relationship('Todo', backref='tipo')


class Todo(db.Model):
    """
    Armazena detalhes da tarefa criada.

    As informações armazenas são nome da tarefa, tipo, e data de entrega.

    """
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(50), null=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipos.id'), null=False)
    finalizado = db.Column(db.Boolean, default=False)
    data_entrega = db.Column(db.DateTime)
