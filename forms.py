from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class User_registration_form(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    login = StringField("Login: ", validators=[DataRequired()])
    email = StringField("Email: ", validators=[Email()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    passwordRepeatFieled = PasswordField("Password again: ", validators=[DataRequired()])
    submit = SubmitField("Submit")
class add_Comment(FlaskForm):
    text = StringField("Text: ", validators=[DataRequired()])
    submit = SubmitField("Submit")
class User_log_in_form(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Submit")