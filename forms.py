from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField, SelectField, PasswordField,
                     TextField, TextAreaField, SubmitField, IntegerField, FileField, ValidationError, DateField)
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed


class profiles(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    image = FileField('Update Image', validators=[
                      FileAllowed(['jpg', 'png', 'jpeg'])])
    budget = IntegerField('Monthly Budget', validators=[DataRequired()])
    income = IntegerField('Monthly Income', validators=[DataRequired()])
    submit = SubmitField('Update')


class loginForm(FlaskForm):
    email1 = StringField('Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    submit1 = SubmitField('Log In')


class registrationForm(FlaskForm):
    username2 = StringField('UserName', validators=[DataRequired()])
    email2 = StringField('Email', validators=[DataRequired(), Email()])
    password2 = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'pass_confirm', message='Passwords must match')])
    pass_confirm = PasswordField(
        'Confirm Password', validators=[DataRequired()])
    submit2 = SubmitField('Register')

    def check_email(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')


class transactionForm(FlaskForm):
    amount = IntegerField('Amount', validators=[DataRequired()])
    date = DateField('Date of Transaction', validators=[DataRequired()])
    description = TextField('Description', validators=[DataRequired()])
    flow = RadioField('', choices=[
                      ('debit', 'Cash In'), ('credit', 'Cash Out')], validators=[DataRequired()])
    submit = SubmitField('Add Transaction')
