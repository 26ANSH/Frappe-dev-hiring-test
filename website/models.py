from . import db
from sqlalchemy.sql import func

class Books(db.Model):
    __tablename__ = 'books'
    id       = db.Column(db.Integer, primary_key=True)
    isbn     = db.Column(db.Integer, nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False)
    title    = db.Column(db.String(100), nullable=False)
    author   = db.Column(db.String(100), nullable=False)
    rating   = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(5), nullable=False)
    book_id  = db.Column(db.Integer, db.ForeignKey('books.id'))

class Members(db.Model):
    __tablename__ = 'members'
    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String(100), nullable=False)
    email     = db.Column(db.String(100), nullable=False)
    phone     = db.Column(db.String(100), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))

class Lms(db.Model):
    __tablename__ = 'transactions'
    id          = db.Column(db.Integer, primary_key=True)
    book_id     = db.Column(db.Integer, db.ForeignKey('books'))
    member_id   = db.Column(db.Integer, db.ForeignKey('members'))
    date        = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
    return_date = db.Column(db.DateTime)
    fine        = db.Column(db.Integer)
    status      = db.Column(db.Boolean, nullable=False)


