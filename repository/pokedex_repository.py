from main import db
from models.pokedex import Pokedex
from models.status import Status

class PokedexRepository:
    @staticmethod
    def search(id: int) -> Pokedex:
        return Pokedex.query.filter_by(id=id).first()
    
    @staticmethod
    def getStatus(id: int) -> Status:
        return Status.query.filter_by(pokemon_id=id).first()
    
    @staticmethod
    def searchAll():
        return Pokedex.query.order_by(Pokedex.id)
        
    @staticmethod
    def create(data: dict, status: list):
        try:
            pokemon = Pokedex(name=data['name'], type_1=data['type_1'], type_2=data['type_2'], ability=data['ability'])
            
            db.session.add(pokemon)
            db.session.commit()
            
            status_pokemon = Status(
                pokemon=pokemon,
                hp=status['hp'],
                atk=status['atk'],
                def_=status['def'],
                spatk=status['spatk'],
                spdef=status['spdef'],
                spd=status['spd'],
            )

            db.session.add(status_pokemon)
            db.session.commit()
            return pokemon
        except:
            return False
    
    @staticmethod
    def update(pokemon: Pokedex, status: Status, data: dict, status_dict: dict):
        try:
            pokemon.name = data['name']
            pokemon.type_1 = data['type_1']
            pokemon.type_2 = data['type_2']
            pokemon.ability = data['ability']
            
            status.hp = status_dict['hp']
            status.atk = status_dict['atk']
            status.def_ = status_dict['def']
            status.spatk = status_dict['spatk']
            status.spdef = status_dict['spdef']
            status.spd = status_dict['spd']

            db.session.commit()
            return pokemon
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
    