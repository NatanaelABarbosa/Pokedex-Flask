from main import db

class Pokedex(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    type_1 = db.Column(db.String(15), nullable=False)
    type_2 = db.Column(db.String(15), nullable=False)
    ability = db.Column(db.String(20), nullable=False)
    
    status = db.relationship("Status", back_populates="pokemon", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return '<Name %r>' % self.name 