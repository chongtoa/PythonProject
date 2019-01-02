from flask import Flask, render_template

app = Flask(__name__)


# # 重定向
# @app.route('/')
# def index():
#     login_url = url_for('login')
#     return redirect(login_url)
#     return '这是首页！'

# 模板渲染以及传参
@app.route('/')
def index():
    context={
        'username': 'hello',
        'age':18,
        'gender': 'male'
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
