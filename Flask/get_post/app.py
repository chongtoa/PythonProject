from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
    print(request.args)
    q = request.args.get('q')
    return 'search'

# 默认的视图函数，只能采用get请求
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        return "post request"



if __name__ == '__main__':
    app.run(debug=True)
