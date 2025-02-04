from main import db
from models.pokedex import Pokedex

class PokedexRepository:
    @staticmethod
    def fetch():
        pass
    
    @staticmethod
    def fetchAll():
        return Pokedex.query.order_by(Pokedex.id)
    
    @staticmethod
    def create(data: dict, status: list):
        try:
            pokemon = Pokedex(nome=data['nome'], tipo=data['tipo'], abilidade=data['abilidade'])
            
            db.session.add(pokemon)
            db.session.commit()
            return True
        except:
            return False
    
    @staticmethod
    def update():
        pass
    
    @staticmethod
    def delete():
        pass
    