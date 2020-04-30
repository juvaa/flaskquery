from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length

class Form(FlaskForm):
    hallitus = TextAreaField('Palautetta hallitukselle toiminnasta:', validators=[Length(max=500)])
    tapahtuma = TextAreaField('Palautetta tapahtumasta:', validators=[Length(max=500)])
    ehdotus = TextAreaField(
        'Ehdotuksia tapahtumasta/aktiviteetista/kiltahuonehankinnasta:', validators=[Length(max=500)])
    muuta = TextAreaField('Muuta, mitä haluat hallituksen tietävän:', validators=[Length(max=500)])
    submit = SubmitField('Lähetä')
