from flask import Blueprint, request, redirect, url_for, render_template, current_app
from flask_login import LoginManager, login_user, logout_user, \
    login_required, current_user
from blog.models.user import User
from sqlalchemy.exc import IntegrityError
from models.models import db
from blog.forms.user import RegistrationForm, LoginForm
from werkzeug.exceptions import NotFound

auth_app = Blueprint('auth_app', __name__)

login_manager = LoginManager()
login_manager.login_view = "auth_app.login"


@auth_app.route("/register/", methods=["POST", "GET"], endpoint="register")
def register():
    if current_user.is_authenticated:
        return redirect('index')

    error = None
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append("email is already exists")
            return render_template("auth/register.html", form=form)

        if User.query.filter_by(username=form.username.data).count():
            form.username.errors.append("username is already exists")
            return render_template("auth/register.html", form=form)

        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            is_staff=False,
        )
        user.password = form.password.data
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create user")
            error = 'Could nor create user'
        else:
            current_app.logger.info(f'Create user {user}')
            login_user(user)
            return redirect(url_for('index'))
    return render_template("auth/register.html", form=form, error=error)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))


@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(
            first_name=form.first_name.data).one_or_none()
        if user is None:
            return render_template("auth/login.html", form=form,
                                   error="User name doen't exist")
        if not user.validate_password(form.password.data):
            return render_template("auth/login.html", form=form,
                                   error="invalid user name or password")

        login_user(user)
        return redirect(url_for('index'))
    return render_template("auth/login.html", form=form)


@auth_app.route("login-as/", methods=["POST", "GET"], endpoint="login-as")
def login_as():
    if not current_user.is_authenticated and current_user.is_staff:
        raise NotFound

@auth_app.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@auth_app.route("/secret/")
@login_required
def secret_view():
    return "Super secret data"


__all__ = [
    "login_manager",
    "auth_app",
]
