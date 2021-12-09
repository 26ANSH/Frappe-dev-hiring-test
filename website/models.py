from . import db
from sqlalchemy.sql import func

class Books(db.Model):
    __tablename__ = 'books'
    id       = db.Column(db.Integer, primary_key=True)
    isbn     = db.Column(db.Integer, nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False)
    issued = db.Column(db.Integer, nullable=False, default=0)
    title    = db.Column(db.String(100), nullable=False)
    author   = db.Column(db.String(100), nullable=False)
    book_id  = db.Column(db.Integer, db.ForeignKey('books.id'))

    def __init__(self, book, quantity):
        self.isbn = book['isbn']
        self.quantity = quantity
        self.title = book['title']
        self.author = book['authors']
        self.book_id = book['bookID']
        
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


