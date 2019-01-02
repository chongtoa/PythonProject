#encoding:utf-8
# 从flask中导入Flask
from flask import Flask, url_for

# 初始化一个Flask对象，参数__name__
app = Flask(__name__)

# 装饰器,反转url
@app.route('/')
def hello_world():
    print(url_for('pages', id='123'))
    return 'index'

# url传参
@app.route('/pages/<id>')
def pages(id):
    return id

if __name__ == '__main__':
    app.run(debug=True)
