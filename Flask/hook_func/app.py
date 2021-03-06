from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'index!'


@app.before_request
def my_before_request():
    print('hello world')

if __name__ == '__main__':
    app.run(debug=True)
