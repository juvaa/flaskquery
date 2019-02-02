from app import db

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    con_irc = db.Column(db.Boolean())
    con_tel = db.Column(db.Boolean())
    con_email = db.Column(db.Boolean())
    organize = db.Column(db.Boolean())
    game = db.Column(db.String(64))
    time = db.Column(db.String(64))
    other = db.Column(db.String(500))
    datetime = db.Column(db.DateTime())
