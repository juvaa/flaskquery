from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Optional, Length

class Form(FlaskForm):
    name = StringField('Nimi*', validators=[DataRequired(), Length(max=64)])
    guild = RadioField('Ryhmä*', choices=(['otit', 'OTiT'],['sik', 'SIK'], ['blanko', 'Blanko'], ['henkilokunta', 'Tiedekunnan henkilöstö']))
    mail = StringField('Sähköpostiosoite*', validators=[DataRequired(), Length(max=64)])
    specialfoods = TextAreaField('Erityisruokavaliot (Vastaa vaikket osallistuisi sitseille)', validators=[Length(max=500)])
    hopesndreams = TextAreaField('Toiveita seminaarissa käsiteltävistä asioista', validators=[Length(max=500)])
    attend = BooleanField('Kyllä')
    alcohol = RadioField('Juomatoive', choices=(['alkoholillinen', 'Alkoholillinen'], ['alkoholiton', 'Alkoholiton']), validators=[Optional()])
    wine = RadioField('Juomatoive', choices=(['punaviini', 'Punaviini'], ['valkoviini', 'Valkoviini']), validators=[Optional()])
    beer = RadioField('Juomatoive', choices=(['olut', 'Olut'], ['siideri', 'Siideri']), validators=[Optional()])
    consent = BooleanField(
        'Hyväksyn henkilötietojeni käsittelyn tietosuojaselosteen mukaisesti, sekä ymmärrän ilmoittatumisen olevan sitova.',
        validators=[InputRequired()])
    submit = SubmitField('Lähetä')
