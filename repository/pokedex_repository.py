from main import db
from models.pokedex import Pokedex

class PokedexRepository:
    def create(data: dict, status: list):
        try:
            pokemon = Pokedex(nome=data['nome'], tipo=data['tipo'], abilidade=data['abilidade'])
            
            db.session.add(pokemon)
            db.session.commit()
            return True
        except:
            return False
    
    def update():
        pass
    
    def fetch():
        pass
    
    def fetchAll():
        pass
    
    def delete():
        pass
    