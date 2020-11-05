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
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class registrationForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'pass_confirm', message='Passwords must match')])
    pass_confirm = PasswordField(
        'Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    # def check_email(self, field):
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError('Your email has been registered already!')


class transactionForm(FlaskForm):
    amount = IntegerField('Amount', validators=[DataRequired()])
    date = DateField('Date of Transaction', validators=[DataRequired()])
    description = TextField('Description', validators=[DataRequired()])
    flow = RadioField('', choices=[
                      ('debit', 'Cash In'), ('credit', 'Cash Out')], validators=[DataRequired()])
    submit = SubmitField('Add Transaction')
