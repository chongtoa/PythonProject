from flask import Flask
from flask_sqlalchemy  import  SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

article_tag = db.Table("article_tag",
                       db.Column("article_id", db.Integer, db.ForeignKey("article.id"), primary_key=True),
                       db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True)
                       )

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)

    tags = db.relationship("Tag", secondary=article_tag, backref=db.backref("article"))
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)

db.create_all()
@app.route('/')
def hello_world():
    # article1 = Article(title="aaa")
    # article2 = Article(title="bbb")
    #
    # tag1 = Tag(title="111")
    # tag2 = Tag(title="222")
    #
    # article1.tags.append(tag1)
    # article1.tags.append(tag2)
    #
    # article2.tags.append(tag1)
    # article2.tags.append(tag2)
    #
    # db.session.add(article1)
    # db.session.add(article2)
    #
    # db.session.add(tag1)
    # db.session.add(tag2)

    article1 = Article.query.filter(Article.title == "aaa").first()
    tags = article1.tags
    for tag in tags:
        print(tag.title)
    # db.session.commit()

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
