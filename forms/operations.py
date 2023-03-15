from wtforms import StringField, TextAreaField, SubmitField, \
    DateField, validators
from flask_wtf import  FlaskForm

class CreateOperationForm(FlaskForm):
    name = StringField('Название операции', [validators.DataRequired()])
    operators = StringField("Оператор", [validators.DataRequired()])
    body = TextAreaField('Протокол операции', [validators.DataRequired()])
    data = DateField('Дата операции', [validators.DataRequired()])
    submit = SubmitField('Добавить')
