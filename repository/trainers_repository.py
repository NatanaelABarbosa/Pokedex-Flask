from main import db
from models.trainers import Trainers
from flask_bcrypt import generate_password_hash, check_password_hash
from flask import session

class TrainersRepository:
    def search(self, nickname: str):
        return Trainers.query.filter_by(nickname=nickname).first() 
    
    def check_if_nickname_exists(self, nickname: str):
        return self.search(nickname) is not None
    
    def check_password(self, nickname, password):
        trainer = self.search(nickname)

        if check_password_hash(trainer.password, password):
            return True
        
        return False
    
    def register(self, trainer: Trainers):
        try:
            trainer.password = generate_password_hash(trainer.password)
            
            db.session.add(trainer)
            db.session.commit()
            self.login(trainer.nickname)

            return True
        except:
            return False
        
    def login(self, nickname):
        session['usuario'] = nickname
        
    @staticmethod
    def logout():
        session['usuario'] = None