from main import db
from models.pokedex import Pokedex

class PokedexRepository:
    @staticmethod
    def search(id: int) -> Pokedex:
        return Pokedex.query.filter_by(id=id).first()
    
    @staticmethod
    def searchAll():
        return Pokedex.query.order_by(Pokedex.id)
        
    @staticmethod
    def create(data: dict, status: list):
        try:
            pokemon = Pokedex(name=data['name'], type_1=data['type_1'], type_2=data['type_2'], ability=data['ability'])
            
            db.session.add(pokemon)
            db.session.commit()
            return pokemon
        except:
            return False
    
    @staticmethod
    def update(pokemon: Pokedex, data: dict, status: dict):
        try:
            pokemon.name = data['name']
            pokemon.type_1 = data['type_1']
            pokemon.type_2 = data['type_2']
            pokemon.ability = data['ability']
            
            db.session.commit()
            return 
        except:
            return False
    
    @staticmethod
    def delete(id: int):
        try:
            Pokedex.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
    