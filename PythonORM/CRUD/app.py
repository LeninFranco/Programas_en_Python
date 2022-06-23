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

def create(book: Book):
    db.session.add(book)
    db.session.commit()

def read_all():
    return Book.query.all()

def read_one(ID: int):
    return Book.query.filter_by(id=ID).first()

def update(book: Book):
    old_book = read_one(book.id)
    old_book.name = book.name
    old_book.author = book.author
    db.session.commit()

def delete(book: Book):
    db.session.delete(book)
    db.session.commit()

if __name__ == "__main__":
    """
    #Create
    b = Book()
    b.name = "ola"
    b.author = "awa"
    create(b)
    """

    """
    #Read One
    b = read_one(1)
    print(b)
    """

    """
    #Read All
    lista = read_all()
    print(lista)
    """

    """
    #Update
    b = read_one(3)
    b.author = "William P. Blatty"
    update(b)
    """

    """
    #Delete
    b = read_one(6)
    delete(b)
    """

