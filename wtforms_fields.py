from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField
from wtforms.validators import InputRequired,Length,EqualTo


class RegistrationForm(FlaskForm):

    username = StringField('username' , 
    validators=[InputRequired(message="username required"),
    Length(min=4,max=25,message="username must be between 4 and 25 characters")])
    password = PasswordField('password', validators=[InputRequired(message="password required"),
    Length(min=4,max=25,message="username must be between 4 and 25 characters")])
    confirm_password = PasswordField('confirm password', validators=[InputRequired(message="password must match"),
    Length(min=4,max=25,message="username must be between 4 and 25 characters")])
    submit_button = SubmitField('Create')