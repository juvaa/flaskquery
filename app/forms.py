from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, SelectField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Optional, Length, NumberRange

class Form(FlaskForm):
    name = StringField('Nimi*', validators=[InputRequired(), Length(max=64)])
    mail = StringField('Sähköpostiosoite*', validators=[InputRequired(), Length(max=64)])
    s_year = IntegerField('Opintojen aloitusvuosi*', validators=[Optional(), NumberRange(min=1900, max=2020)])
    specialfoods = TextAreaField('Erityisruokavaliot', validators=[Optional(), Length(max=500)])
    drink = RadioField('Juomatoive', choices=(['alkoholillinen', 'Alkoholillinen'], ['alkoholiton', 'Alkoholiton']), validators=[InputRequired()])
    alcohol_wish = RadioField('Juomatoive', choices=(['jallu', 'Jallu'], ['kahvilikööri', 'Kahvilikööri']), validators=[Optional()])
    none_wish = StringField('Juomatoive', validators=[Optional(), Length(max=64)])
    sillis = BooleanField('Osallistun sillikseen', validators=[Optional()])
    greeting = BooleanField('Tuon tervehdyksen', validators=[Optional()])
    greeter = StringField('Edustettu taho', validators=[Optional(), Length(max=64)])
    avec = BooleanField('Avec', validators=[Optional()])
    avec_name = StringField('Avecin nimi', validators=[Optional(), Length(max=64)])
    avec_specialfoods = TextAreaField('Erityisruokavaliot', validators=[Optional(), Length(max=500)])
    avec_drink = RadioField('Juomatoive', choices=(['alkoholillinen', 'Alkoholillinen'], ['alkoholiton', 'Alkoholiton']), validators=[Optional()])
    avec_alcohol_wish = RadioField('Juomatoive', choices=(['jallu', 'Jallu'], ['kahvilikööri', 'Kahvilikööri']), validators=[Optional()])
    avec_none_wish = StringField('Juomatoive', validators=[Optional(), Length(max=64)])
    history = BooleanField('Haluan tilata historiikin', validators=[Optional()])
    table = StringField('Pöytätoive', validators=[Optional(), Length(max=64)])
    name_consent = BooleanField(
        'Haluan, että nimeni julkaistaan osallistuvien listalla')
    consent = BooleanField(
        'Hyväksyn henkilötietojeni käsittelyn tietosuojaselosteen mukaisesti, sekä ymmärrän ilmoittatumisen olevan sitova.*',
        validators=[InputRequired()])
    submit = SubmitField('Lähetä')
