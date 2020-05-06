from app import db

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    mail = db.Column(db.String(64))
    s_year = db.Column(db.String(4))
    specialfoods = db.Column(db.String(500))
    sillis = db.Column(db.Boolean())
    greeting = db.Column(db.String(64))
    avek = db.Column(db.String(64))
    history = db.Column(db.Boolean())
    table = db.Column(db.String(64))
    name_consent = db.Column(db.Boolean())
    datetime = db.Column(db.DateTime())

class Invite_register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    mail = db.Column(db.String(64))
    s_year = db.Column(db.String(64))
    specialfoods = db.Column(db.String(500))
    sillis = db.Column(db.Boolean())
    greeting = db.Column(db.String(64))
    avek = db.Column(db.String(64))
    history = db.Column(db.Boolean())
    table = db.Column(db.String(64))
    name_consent = db.Column(db.Boolean())
    datetime = db.Column(db.DateTime())
