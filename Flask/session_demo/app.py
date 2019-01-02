import os
from flask import Flask, session
from datetime import  timedelta
app = Flask(__name__)

app.config["SECRET_KEY"]=os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
# add session to data


@app.route('/')
def hello_world():
    session["username"] = "chongtao"
    session.permanent=True
    return 'Hello World!'


@app.route('/get/')
def get():
    return session.get('username')

@app.route('/delete/')
def delete():
    session.pop('username')
    return 'succed'

@app.route('/clear/')
def clear():
    session.clear()
    return 'succed'


if __name__ == '__main__':
    app.run(debug=True)
