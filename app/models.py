from app import db

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hallitus = db.Column(db.String(500))
    tapahtuma = db.Column(db.String(500))
    ehdotus = db.Column(db.String(500))
    muuta = db.Column(db.String(500))
    datetime = db.Column(db.DateTime())
    arkisto = db.Column(db.Boolean())
