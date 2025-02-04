from main import db

class Pokedex(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(15), nullable=False)
    abilidade = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.nome