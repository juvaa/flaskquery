from app import db

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    guild = db.Column(db.String(64))
    mail = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    place = db.Column(db.String(64))
    cruise = db.Column(db.Boolean())
    buffet = db.Column(db.Boolean())
    datetime = db.Column(db.DateTime())
