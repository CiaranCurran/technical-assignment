from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class wordCountForm(FlaskForm):
    word = StringField('Word to be counted...', validators=[DataRequired()])
    url = StringField('URL to be searched...', validators=[DataRequired(), URL()])
    submit = SubmitField('Count Word')
