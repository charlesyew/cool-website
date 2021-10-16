from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators 
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from script.models import User

class RegistrationForm(FlaskForm): 
    username = StringField('Username', validators = [DataRequired(), Length(min = 6, max = 12)])
    email = StringField('Email', validators = [Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username): 
        user = User.query.filter_by(username = username.data).first()
        if user: 
            raise ValidationError('That username is taken. Please choose another one.')

    def validate_email(self, email): 
        email = User.query.filter_by(email = email.data).first()
        if email: 
            raise ValidationError('Your email is associated with an account. Please go to login page.')

class LoginForm(FlaskForm): 
    email = StringField('Email', validators = [Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')