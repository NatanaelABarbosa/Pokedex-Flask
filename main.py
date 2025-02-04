import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt 

app = Flask(__name__)
app.config.from_pyfile(os.path.dirname(os.path.abspath(__file__)) + '/config/config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

from routes.web import *

if __name__ == "__main__":
    app.run(debug=True)