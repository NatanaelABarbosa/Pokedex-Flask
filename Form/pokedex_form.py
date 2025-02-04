from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length

class PokedexForm(FlaskForm):
    name = StringField(
        "Nome",
        validators=[DataRequired(), Length(min=1, max=50)]
    )
    
    ability = StringField(
        "Abilidade",
        validators=[DataRequired(), Length(min=1, max=20)]
    )
    
    type = SelectField('Tipo do Pokémon', choices=[
            ('fogo', 'Fogo'),
            ('agua', 'Água'),
            ('planta', 'Planta'),
            ('eletrico', 'Elétrico'), 
            ('inseto', 'Inseto'), 
            ('sombrio', 'Sombrio'), 
            ('dragao', 'Dragão'), 
            ('fada', 'Fada'), 
            ('lutador', 'Lutador'), 
            ('voador', 'Voador'), 
            ('terra', 'Terra'), 
            ('gelo', 'Gelo'), 
            ('normal', 'Normal'), 
            ('venenoso', 'Venenoso'), 
            ('psiquico', 'Psíquico'), 
            ('pedra', 'Pedra'), 
            ('metal', 'Metal'), 
            ('fantasma', 'Fantasma'), 
        ],
        validators=[DataRequired()]
    )