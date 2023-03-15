from flask import Flask
from flask import Blueprint, render_template
from config.security import flask_bcrypt
from config.config import DeveloperPostgresConfig
from flask_migrate import Migrate
from models.init_dba import db
from commands import my_cli_commands
from views.auth import login_manager, auth_app

app = Flask(__name__)

#blueprints
app.register_blueprint(my_cli_commands)
app.register_blueprint(auth_app, url_prefix='/auth')
#settings
app.config.from_object(DeveloperPostgresConfig)
#imports

flask_bcrypt.init_app(app)
login_manager.init_app(app)
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db, compare_type=True)
#logger


@app.route('/')
def index():
    return render_template("index.html")




if __name__ == '__main__':
    app.run()
