import os

from models.init_dba import db
from flask import logging, Blueprint
from dotenv import load_dotenv
from models.models import User
from colorama import Fore

load_dotenv()
my_cli_commands = Blueprint('init_db', __name__)

@my_cli_commands.cli.command('create_user')
def create_user():
    """
    Create admin user in db
    :return:
    """
    admin = User(name='admin')
    admin.password = os.getenv('FLASK_DB_PASS')
    db.session.add(admin)
    db.session.commit()

    logging.info(f'Создан юзер в бд {admin.name}, {admin.id}')
    print(Fore.GREEN + f'Создан юзер в бд {admin.name}, {admin.id}' + Fore.RESET)




