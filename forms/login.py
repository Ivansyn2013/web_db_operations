from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, validators
class LoginForm(FlaskForm):
    first_name = StringField("Имя пользователя", [validators.DataRequired()])
    password = PasswordField("Пароль", [validators.DataRequired()])
    submit = SubmitField("Войти")