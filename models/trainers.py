from main import db

class Trainers(db.Model):
    name = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(8), primary_key=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Nickname %r>' % self.nickname 