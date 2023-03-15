from flask import Blueprint, render_template, request, redirect, url_for
from models.models import Operation
from flask_login import login_required
from forms.operations import CreateOperationForm
from models.init_dba import db
from sqlalchemy.exc import IntegrityError

operations_app = Blueprint('operations_app', __name__)

@operations_app.route('/', endpoint='list')
@login_required
def operations_list():
    operations = Operation.query.all()
    return render_template('operations/list.html', operations=operations)


@operations_app.route('/create', methods=['GET'], endpoint='create')
@login_required
def operations_create():
    form = CreateOperationForm(request.form)
    return render_template('operations/create.html', form=form)

@operations_app.route('/create', methods=['POST'], endpoint='create_db')
@login_required
def operarions_create():
    form = CreateOperationForm(request.form)
    if form.validate_on_submit():
        operation = Operation(name=form.name.data,
                              operators=form.operators.data,
                              body=form.body.data,
                              data=form.data.data,
                              )
        try:
            db.session.add(operation)
            db.session.commit()
        except IntegrityError as error:
            print(f'Ошибка операций бд {error}')
        return redirect(url_for('operations_app.list'))
    else:
        return render_template(operations_create, error='error db')