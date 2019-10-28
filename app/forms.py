from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Optional

class Form(FlaskForm):
    name = StringField('Nimi*', validators=[DataRequired()])
    mail = StringField('Sähköpostiosoite*', validators=[DataRequired()])
    operator = BooleanField('Olen operaattori')
    alcohol = RadioField('Juomatoive', choices=(['alkoholillinen', 'Alkoholillinen'], ['alkoholiton', 'Alkoholiton']))
    wine = RadioField('Juomatoive', choices=(['punaviini', 'Punaviini'], ['valkoviini', 'Valkoviini']), validators=[Optional()])
    beer = RadioField('Juomatoive', choices=(['olut', 'Olut'], ['siideri', 'Siideri']), validators=[Optional()])
    specialneeds = TextAreaField('Allergiat ja erityisruokavaliot')
    consent = BooleanField(
        'Hyväksyn henkilötietojeni käsittelyn tietosuojaselosteen mukaisesti, sekä ymmärrän ilmoittatumisen olevan sitova.',
        validators=[InputRequired()])
    gdpr = BooleanField(
        'Nimeni saa julkaista tällä sivulla.')

    avec = BooleanField('Avec')
    avec_name = StringField('Avecin nimi*')
    avec_alcohol = RadioField('Juomatoive', choices=(['alkoholillinen', 'Alkoholillinen'], ['alkoholiton', 'Alkoholiton']), validators=[Optional()])
    avec_wine = RadioField('Juomatoive', choices=(['punaviini', 'Punaviini'], ['valkoviini', 'Valkoviini']), validators=[Optional()])
    avec_beer = RadioField('Juomatoive', choices=(['olut', 'Olut'], ['siideri', 'Siideri']), validators=[Optional()])
    avec_specialneeds = TextAreaField('Allergiat ja erityisruokavaliot')
    avec_consent = BooleanField(
        'Avecini hyväksyy hänen henkilötietojensa käsittelyn tietosuojaselosteen mukaisesti.', default="checked", validators=[InputRequired()])

    avec_gdpr = BooleanField(
        'Avecini nimen saa julkaista tällä sivulla.')
    submit = SubmitField('Submit')
