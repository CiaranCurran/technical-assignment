from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class WordCountForm(FlaskForm):
    word = StringField('Word to be counted...', validators=[DataRequired()])
    url = StringField('URL to be searched...', validators=[DataRequired(), URL()])
    submit = SubmitField('Count Word')
