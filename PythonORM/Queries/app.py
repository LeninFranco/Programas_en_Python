from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    author = db.Column(db.String(50))

    def __repr__(self):
        return f'<id: {self.id}, name: {self.name}, author: {self.author}>' 

def select_all():
    return Book.query.all()

def select_one_by_ID(ID: int):
    return Book.query.filter_by(id=ID).first()

def count_rows():
    return Book.query.count()

def filter_by_name():
    return Book.query.filter_by(author='Stephen King').all()

def custom_query():
    return db.engine.execute('SELECT * FROM book')

if __name__ == "__main__":
    r = custom_query()
    for i in r:
        print(i)