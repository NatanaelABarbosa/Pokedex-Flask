import os

SECRET_KEY = 'chave_secreta'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'N4ellean.',
        servidor = 'localhost',
        database = 'pokedex',
    )
    
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'