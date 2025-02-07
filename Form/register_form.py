from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    name = StringField(
        "Nome",
        validators=[DataRequired(), Length(min=1, max=20)]
    )
    
    nickname = StringField(
        "Nickname",
        validators=[DataRequired(), Length(min=1, max=8)]
    )
    
    password = PasswordField(
        "Senha",
        validators=[DataRequired(), Length(min=1, max=100)]
    )