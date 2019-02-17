# encoding: utf-8
from flask_script import Manager
from app import app_demo
from  db_scripts import DBManager

manager = Manager(app_demo)


@manager.command
def runserver():
    print("server is running!")


manager.add_command('db', DBManager)

if __name__ == '__main__':
    manager.run()