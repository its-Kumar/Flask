import wtforms
from flask_wtf import FlaskForm
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)

from market.models import User


class RegisterForm(FlaskForm):
    username = wtforms.StringField(
        label='User Name:',
        validators=[Length(min=2, max=30), DataRequired()])
    email_address = wtforms.StringField(
        label="Email Address:",
        validators=[Email(), DataRequired()])
    password1 = wtforms.PasswordField(
        label='Password:',
        validators=[Length(min=6), DataRequired()])
    password2 = wtforms.PasswordField(
        label='Confirm Password:',
        validators=[EqualTo('password1'), DataRequired()])

    submit = wtforms.SubmitField(label='Create Account')

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(
                'Username already exists! Please try a diffrent username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(
            email_address=email_address_to_check.data).first()

        if email_address:
            raise ValidationError(
                'Email Address is already exixts! Please try a different email\
                    address')


class LoginForm(FlaskForm):
    username = wtforms.StringField(
        label='User Name:', validators=[DataRequired()])
    password = wtforms.PasswordField(
        label='Password:', validators=[DataRequired()])
    submit = wtforms.SubmitField(label='Log In')


class PurchaseItemForm(FlaskForm):
    submit = wtforms.SubmitField(label="Purchase Item!")


class SaleItemForm(FlaskForm):
    submit = wtforms.SubmitField(label="Sale Item!")
