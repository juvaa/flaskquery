from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    nick = StringField('Nimimerkki*', validators=[DataRequired()])
    email = StringField('Sähköposti*', validators=[DataRequired()])
    phone = StringField('Puhelinnumero')
    con_irc = BooleanField('IRC-Netistä')
    con_tel = BooleanField('Telegrammista')
    con_email = BooleanField('Sähköpostise')
    organize = BooleanField('Olen kiinnostunut!')
    game = StringField('Peli jonka haluaisit pelata')
    time = StringField('Pelin suurinpiirteinen kesto')
    other = TextAreaField('Muuta kerrottavaa')
    consent = BooleanField('Lupaan merkitä tapahtuman kalenteriini ja teen kaikkeni jotta voin siihen osallistua*')
    gdpr_consent = BooleanField('Hyväksyn henkilötietojeni käsittelyn tietosuojaselosteen mukaisesti*')
    submit = SubmitField('Lähetä')
