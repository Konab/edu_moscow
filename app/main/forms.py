from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    name = TextAreaField('Say Your Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

