from app import db, ma


class Tipo(db.Model):
    """
    Armazena as informações relacionadas ao tipo de tarefa.

    Os tipos pré-cadastrados são Pessoal e Profissional. No entanto, a plataforma
    permite que os tipos sejam expandidos de acordo com a necessidade.

    """
    __tablename__ = 'tipos'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)
    todos = db.relationship('Todo', backref='tipo')

    def __str__(self):
        return '<Tipo: {}>'.format(self.tipo)

    def __repr__(self):
        return '<Tipo: {}>'.format(self.tipo)


class TipoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'tipo')

class Todo(db.Model):
    """
    Armazena detalhes da tarefa criada.

    As informações armazenas são nome da tarefa, tipo, e data de entrega.

    """
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(50), nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipos.id'), nullable=False)
    finalizado = db.Column(db.Boolean, default=False)
    data_entrega = db.Column(db.DateTime)

    def __str__(self):
        return '<Todo: {}>'.format(self.todo)

    def __repr__(self):
        return '<Todo: {}>'.format(self.todo)


class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'todo', 'tipo_id', 'finalizado', 'data_entrega')
