from main import db
from models.pokedex import Pokedex

class Status(db.Model):
    __tablename__ = "pokemon_status"

    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokedex.id", ondelete="CASCADE"), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    atk = db.Column(db.Integer, nullable=False)
    def_ = db.Column("def", db.Integer, nullable=False)  
    spatk = db.Column(db.Integer, nullable=False)
    spdef = db.Column(db.Integer, nullable=False)
    spd = db.Column(db.Integer, nullable=False)

    pokemon = db.relationship("Pokedex", back_populates="status")