from app import db

class Model(db.Model):
    DonationId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    Amount = db.Column(db.Float)
    Message = db.Column(db.String(1024))
    MessageAnswer = db.Column(db.String(1024))
    CollectorImageUrl = db.Column(db.String(128))
    CurrencySymbol = db.Column(db.String(64))
    CollectionUrl = db.Column(db.String(128))
    TransactionDate = db.Column(db.String(64))
    activationstamp = db.Column(db.String(64))
