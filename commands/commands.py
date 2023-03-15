import os

from models.init_dba import db
from flask import Blueprint
from sqlalchemy.exc import IntegrityError
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
    admin = User()
    admin.email = 'example@email.com'
    admin.name = input('Введи имя пользователя:\n')
    tmp = input('Введи пароль пользователя:\n')
    tmp1 = input('Введи пароль пользователя:\n')
    if tmp1 == tmp:
        admin.password = tmp
        db.session.add(admin)
        try:
            db.session.commit()
            print(
                Fore.GREEN + f'Создан юзер в бд {admin.name}, {admin.id}' + Fore.RESET)
        except IntegrityError as error:
            print(Fore.RED + f'Ошибка бд {error}' +Fore.RESET)



    else:
        print(Fore.RED + f'Ошибка. Пароли не одинаковы' + Fore.RESET)
