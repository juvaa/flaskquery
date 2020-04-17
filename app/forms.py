from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    hallitus = TextAreaField('Palautetta hallitukselle toiminnasta:')
    tapahtuma = TextAreaField('Palautetta tapahtumasta:')
    ehdotus = TextAreaField(
        'Ehdotuksia tapahtumasta/aktiviteetista/kiltahuonehankinnasta:')
    muuta = TextAreaField('Muuta, mitä haluat hallituksen tietävän:')
    submit = SubmitField('Lähetä')
