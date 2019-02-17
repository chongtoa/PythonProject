#encoding:utf-8
from flask import g

def log_login():
    print('当前登陆的用户是：%s' %g.username)

