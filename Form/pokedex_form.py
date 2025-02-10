from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class BaseStatusForm(FlaskForm):
    
    def status_validators(): 
        return IntegerField(
            validators=[
                DataRequired(),
                NumberRange(min=1, max=999)
            ]
        ) 

class PokedexForm(BaseStatusForm):
    name = StringField(
        "Nome",
        validators=[DataRequired(), Length(min=1, max=50)]
    )
    
    ability = StringField(
        "Abilidade",
        validators=[DataRequired(), Length(min=1, max=20)]
    )
    
    type_1 = SelectField(
        'Tipo do Pokémon',
        choices = [
            ('Fogo', 'Fogo'),
            ('Água', 'Água'),
            ('Planta', 'Planta'),
            ('Elétrico', 'Elétrico'), 
            ('Inseto', 'Inseto'), 
            ('Sombrio', 'Sombrio'), 
            ('Dragão', 'Dragão'), 
            ('Fada', 'Fada'), 
            ('Lutador', 'Lutador'), 
            ('Voador', 'Voador'), 
            ('Terra', 'Terra'), 
            ('Gelo', 'Gelo'), 
            ('Normal', 'Normal'), 
            ('Venenoso', 'Venenoso'), 
            ('Psíquico', 'Psíquico'), 
            ('Pedra', 'Pedra'), 
            ('Metal', 'Metal'), 
            ('Fantasma', 'Fantasma'), 
        ],
        validators=[DataRequired()]
    )
        
    type_2 = SelectField(
        'Tipo 2 do Pokémon',
        choices = [
            (None, 'Nulo'),
            ('Fogo', 'Fogo'),
            ('Água', 'Água'),
            ('Planta', 'Planta'),
            ('Elétrico', 'Elétrico'), 
            ('Inseto', 'Inseto'), 
            ('Sombrio', 'Sombrio'), 
            ('Dragão', 'Dragão'), 
            ('Fada', 'Fada'), 
            ('Lutador', 'Lutador'), 
            ('Voador', 'Voador'), 
            ('Terra', 'Terra'), 
            ('Gelo', 'Gelo'), 
            ('Normal', 'Normal'), 
            ('Venenoso', 'Venenoso'), 
            ('Psíquico', 'Psíquico'), 
            ('Pedra', 'Pedra'), 
            ('Metal', 'Metal'), 
            ('Fantasma', 'Fantasma'), 
        ],
        validators=[DataRequired()]
    )
    
    hp = BaseStatusForm.status_validators()
    atk = BaseStatusForm.status_validators()
    def_ = BaseStatusForm.status_validators()
    spatk = BaseStatusForm.status_validators()
    spdef = BaseStatusForm.status_validators()
    spd = BaseStatusForm.status_validators()
    