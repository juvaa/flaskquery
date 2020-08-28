from app import db

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    guild = db.Column(db.String(64))
    mail = db.Column(db.String(64))
    specialfoods = db.Column(db.String(500))
    alcohol = db.Column(db.String(64))
    wine = db.Column(db.String(64))
    beer = db.Column(db.String(64))
    name_consent = db.Column(db.String(64))
    datetime = db.Column(db.DateTime())
