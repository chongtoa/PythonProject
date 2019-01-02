#encoding:utf-8
from flask import Flask, render_template,g,request
from utils import log_login

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'index'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'chongtao' and password == '123456':
            # log_login()
            g.username = 'chongtao'
            log_login()
            return '登陆成功'
        else:
            return '登陆密码错误'
        # return 'request OK'


if __name__ == '__main__':
    app.run()
