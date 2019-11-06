from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, InputRequired, Optional

class Form(FlaskForm):
    amount = IntegerField('Amount')
    name = StringField('Name')
    message = StringField('Message')
    submit = SubmitField('Submit')
