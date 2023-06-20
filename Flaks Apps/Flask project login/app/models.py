from . import db, app
from flask_migrate import Migrate
from flask_login import UserMixin


Migrate(app, db)


class User(UserMixin, db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


publisher_author = db.Table('publisher_author',
                    db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
                    db.Column('author_id', db.Integer, db.ForeignKey('authors.id')))


class Books(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'), nullable=False)
    authors = db.relationship('Author', secondary='publisher_author', backref='books')

    def __init__(self, title, description, price, quantity, publisher_id):
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.publisher_id = publisher_id


class Author(db.Model):

    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)


class Publisher(db.Model):

    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    books = db.relationship('Books', backref='publisher')

    def __init__(self, name):
        self.name = name
