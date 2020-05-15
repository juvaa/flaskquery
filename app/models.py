from app import db

class Hallitus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    palaute = db.Column(db.String(500))
    nimi = db.Column(db.String(64))
    email = db.Column(db.String(64))
    datetime = db.Column(db.DateTime())
    arkisto = db.Column(db.Boolean())

class Tapahtuma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    palaute = db.Column(db.String(500))
    nimi = db.Column(db.String(64))
    email = db.Column(db.String(64))
    datetime = db.Column(db.DateTime())
    arkisto = db.Column(db.Boolean())

class Ehdotus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    palaute = db.Column(db.String(500))
    nimi = db.Column(db.String(64))
    email = db.Column(db.String(64))
    datetime = db.Column(db.DateTime())
    arkisto = db.Column(db.Boolean())

class Muuta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    palaute = db.Column(db.String(500))
    nimi = db.Column(db.String(64))
    email = db.Column(db.String(64))
    datetime = db.Column(db.DateTime())
    arkisto = db.Column(db.Boolean())
