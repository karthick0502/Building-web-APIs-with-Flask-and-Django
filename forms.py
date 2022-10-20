from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField # it is used for parse users information
from wtforms.validators import DataRequired, length, Email, EqualTo # we can make some validation in our parsing variable


class RegistrationForm(FlaskForm): # Create a Registration form
    username = StringField('username', validators=[DataRequired(),length(min=2, max=20)])
    Email = StringField('Email', validators=[DataRequired(),Email()])
    Password = PasswordField('Password', validators=[DataRequired()])
    Confirm_Password = Password('Confirm password', validators=[DataRequired(), EqualTo('Password')])
    Submit=SubmitField('Sign Up')


class LoginForm(FlaskForm): # Create a Login form

    Email = StringField('Email', validators=[DataRequired(), Email()])
    Password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    Submit = SubmitField('Log in')