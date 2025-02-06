from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    nickname = StringField(
        "Nickname",
        validators=[DataRequired(), Length(min=1, max=8)]
    )
    
    password = StringField(
        "Senha",
        validators=[DataRequired(), Length(min=1, max=100)]
    )