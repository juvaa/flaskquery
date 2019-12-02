from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Optional

class Form(FlaskForm):
    name = StringField('Nimi* / Name*', validators=[DataRequired()])
    mail = StringField('Sähköpostiosoite* / Email*', validators=[DataRequired()])
    guild = RadioField('Kilta / Guild', choices=(['otit', 'OTiT'], ['olo', 'OLO']))
    alcohol = RadioField('Juomatoive', choices=(['alkoholillinen', 'Alkoholillinen / Alcoholic'], ['alkoholiton', 'Alkoholiton / Non-alcoholic']))
    wine = RadioField('Juomatoive', choices=(['punaviini', 'Punaviini / Red'], ['valkoviini', 'Valkoviini / White']), validators=[Optional()])
    beer = RadioField('Juomatoive', choices=(['olut', 'Olut / Beer'], ['siideri', 'Siideri / Cider']), validators=[Optional()])
    specialneeds = TextAreaField('Allergiat ja erityisruokavaliot / Allergies and special needs')
    consent = BooleanField(
        'Hyväksyn henkilötietojeni käsittelyn tietosuojaselosteen mukaisesti, sekä ymmärrän ilmoittatumisen olevan sitova. / I agree to the processing of my personal data in accordance with this Privacy Policy and understand that the form is binding.',
        validators=[InputRequired()])
    gdpr = BooleanField(
        'Nimeni saa julkaista tällä sivulla. / I allow listing my name below')

    submit = SubmitField('Submit')
