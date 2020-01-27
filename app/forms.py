from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Optional
import os

appurl = os.environ.get("URL")

class Form(FlaskForm):
    name = StringField('Nimi*', validators=[DataRequired()])
    guild = RadioField('Kilta', choices=(['otit', 'OTiT'], ['communica', 'Communica'], ['prose', 'Prose']))
    alcohol = RadioField('Juomatoive', choices=(['alkoholillinen', 'Alkoholillinen'], ['alkoholiton', 'Alkoholiton']))
    wine = RadioField('Juomatoive', choices=(['punaviini', 'Punaviini'], ['valkoviini', 'Valkoviini']), validators=[Optional()])
    beer = RadioField('Juomatoive', choices=(['olut', 'Olut'], ['siideri', 'Siideri']), validators=[Optional()])
    specialneeds = TextAreaField('Allergiat ja erityisruokavaliot')
    consent = BooleanField(
        'Hyväksyn henkilötietojeni käsittelyn <a target = "_blank" href = "{}/static/tietosuojaseloste.pdf" > tietosuojaselosteen </a> mukaisesti, sekä ymmärrän ilmoittatumisen olevan sitova.'.format(appurl),
        validators=[InputRequired()])

    avec = BooleanField('Avec')
    avec_name = StringField('Avecin nimi*')
    avec_alcohol = RadioField('Juomatoive', choices=(['alkoholillinen', 'Alkoholillinen'], ['alkoholiton', 'Alkoholiton']), validators=[Optional()])
    avec_wine = RadioField('Juomatoive', choices=(['punaviini', 'Punaviini'], ['valkoviini', 'Valkoviini']), validators=[Optional()])
    avec_beer = RadioField('Juomatoive', choices=(['olut', 'Olut'], ['siideri', 'Siideri']), validators=[Optional()])
    avec_specialneeds = TextAreaField('Allergiat ja erityisruokavaliot')
    other = TextAreaField('Lisätietoja')
    avec_consent = BooleanField(
        'Avecini hyväksyy hänen henkilötietojensa käsittelyn <a target = "_blank" href = "{}/static/tietosuojaseloste.pdf" > tietosuojaselosteen </a> mukaisesti.'.format(appurl), default="checked", validators=[InputRequired()])

    submit = SubmitField('Submit')
