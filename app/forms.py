from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL

class WordCountForm(FlaskForm):
    word = StringField('Word to be counted...', validators=[DataRequired()])
    url = StringField('URL to be searched...', validators=[DataRequired(), URL()])
    case = BooleanField('Case sensitive search')
    submit = SubmitField('Count Word')

