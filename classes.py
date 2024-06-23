from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import UserMixin

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(16), nullable=False)


class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    age = db.Column(db.Integer)
    books = db.relationship('Book', backref='student', cascade="all, delete-orphan")

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    published = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))

    def __init__(self, name, author, published, student_id=0):
        self.name = name
        self.author = author
        self.published = published
        self.student_id = student_id
