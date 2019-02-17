from flask import Flask
from flask_sqlalchemy  import  SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)

# 创建一个表
class Article(db.Model):

    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # 反向引用
    author = db.relationship("User", backref=db.backref("article"))

# 映射
db.create_all()

@app.route('/')
def index():
    # 添加用户
    # user1 = User(username="zhidao")
    # db.session.add(user1)
    # db.session.commit()

    # 添加文章
    # article1 = Article(title="aaa", content="bbb", author_id=1)
    # db.session.add(article1)
    # db.session.commit()
    article = Article.query.filter(Article.title == "aaa").first()
    # author_id = article.author_id
    # user = User.query.filter(User.id == author_id).first()
    # print(user.username)

    return 'index!'


if __name__ == '__main__':
    app.run(debug=True)
