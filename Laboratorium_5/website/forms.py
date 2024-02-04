from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Enter correct email.')])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Enter correct email.')])
    password = PasswordField('Password', validators=[InputRequired()])
    password_confirm = PasswordField('Confirm password', validators=[InputRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')


class PostForm(FlaskForm):
    content = TextAreaField('Content', validators=[InputRequired(), Length(max=10000)])
    submit = SubmitField('Post')


class ThreadForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(max=255)])
    first_post_content = TextAreaField('Content', validators=[InputRequired(), Length(max=10000)])
    submit = SubmitField('Create Thread')