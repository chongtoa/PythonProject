from flask import Flask

app_demo = Flask(__name__)


@app_demo.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app_demo.run(debug=True)
