# encoding: utf-8

from flask import Flask
from exits import db
import  config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)




# db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
