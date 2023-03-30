from wtforms import StringField, TextAreaField, SubmitField, \
    DateField, validators, TimeField
from flask_wtf import  FlaskForm

class CreateOperationForm(FlaskForm):
    name = StringField('Название операции', [validators.DataRequired()])
    operators = StringField("Хирург", [validators.DataRequired()])
    body = TextAreaField('Протокол операции',
                         [validators.DataRequired()],
                         render_kw={'rows':'30'})
    data = DateField('Дата операции', [validators.DataRequired()])
    nurse = StringField("Медсестра", [validators.DataRequired()])
    start_time = TimeField('Время начала операции', [validators.DataRequired()])
    end_time = TimeField('Время окончания операции',
                         [validators.DataRequired()])


    submit = SubmitField('Добавить')
