from . import db
from datetime import datetime

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    biography = db.Column(db.Text)
    gender = db.Column(db.String(8))
    image = db.Column(db.LargeBinary)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    email = db.Column(db.String(120), unique=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __init__(self, first_name, last_name, username, age, biography, gender, image, created_on, email):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.age=age
        self.biography=biography
        self.gender=gender
        self.image=image
        self.created_on=created_on
        self.email=email
    
    
    def __repr__(self):
        return '<User %r>' % (self.username)
