from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class Post(FlaskForm):
    """Model for feedback."""

    text = TextAreaField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit")
