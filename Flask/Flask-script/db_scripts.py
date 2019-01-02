#encoding: utf-8

from flask_script import Manager
DBManager = Manager()

@DBManager.command
def init():
    print("database init finished!")

@DBManager.command
def migrate():
    print("迁移")