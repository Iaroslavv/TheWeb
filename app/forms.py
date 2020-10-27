from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, validators
from wtforms.validators import DataRequired


class Post(FlaskForm):
    """Model for feedback."""

    text = TextAreaField(validators=[DataRequired(),
                                     validators.Length(max=35)]
                         )
    submit = SubmitField("Submit")


class Email(FlaskForm):
    text = TextAreaField("Email message", validators=[DataRequired()])
    title = StringField("Subject", validators=[DataRequired()])
    submit = SubmitField("Submit")
