from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length ,Email, EqualTo


class RegistrationForm(Form):
    username = StringField('userName', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('enter password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_enter password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Sign Up')

