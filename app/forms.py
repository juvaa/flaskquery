from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Optional, Length

class Form(FlaskForm):
    name = StringField('Nimi*', validators=[DataRequired(), Length(max=64)])
    guild = RadioField('Ryhmä*', choices=(['fuksi', 'Fuksi'],['pro', 'Pro'], ['hallitus', 'Hallitus']), validators=[InputRequired()])
    mail = StringField('Sähköpostiosoite*', validators=[DataRequired(), Length(max=64)])
    specialfoods = TextAreaField('Erityisruokavaliot', validators=[Length(max=500)])
    alcohol = RadioField('Juomatoive', choices=(['alkoholillinen', 'Alkoholillinen'], ['alkoholiton', 'Alkoholiton']), validators=[InputRequired()])
    wine = RadioField('Juomatoive', choices=(['punaviini', 'Punaviini'], ['valkoviini', 'Valkoviini']), validators=[Optional()])
    beer = RadioField('Juomatoive', choices=(['olut', 'Olut'], ['siideri', 'Siideri']), validators=[Optional()])
    name_consent = BooleanField('Haluan, että nimeni julkaistaan osallistujalistalla.')
    consent = BooleanField(
        'Hyväksyn henkilötietojeni käsittelyn tietosuojaselosteen mukaisesti, sekä ymmärrän ilmoittatumisen olevan sitova.*',
        validators=[InputRequired()])    
    corona = BooleanField('Ymmärrän, että flunssaoireisena tai sairaana en tule sitseille.*', validators=[InputRequired()])
    submit = SubmitField('Lähetä')
