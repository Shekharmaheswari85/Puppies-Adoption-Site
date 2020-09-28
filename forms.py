from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


class AddForm(FlaskForm):
    name = StringField('Name of the Puppy:')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):
    id = IntegerField("Id Number of the Puppy to Remove:")
    submit = SubmitField("Remove Puppy")
