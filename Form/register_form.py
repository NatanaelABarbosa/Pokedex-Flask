from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(min=1, max=20)]
    )
    
    nickname = StringField(
        "Nickname",
        validators=[DataRequired(), Length(min=1, max=8)]
    )
    
    password = StringField(
        "Senha",
        validators=[DataRequired(), Length(min=1, max=100)]
    )