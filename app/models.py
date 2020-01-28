from app import db

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    avec = db.Column(db.Boolean())
    name = db.Column(db.String(64))
    mail = db.Column(db.String(64))
    guild =  db.Column(db.String(64))
    alcohol = db.Column(db.String(64))
    wine = db.Column(db.String(64))
    beer = db.Column(db.String(64))
    specialneeds = db.Column(db.String(500))
    avec_name = db.Column(db.String(64))
    other = db.Column(db.String(500))

    datetime = db.Column(db.DateTime())
