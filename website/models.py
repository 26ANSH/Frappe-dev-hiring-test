from . import db
from sqlalchemy.sql import func, select

issued = db.Table('issued',
    db.Column("id", db.Integer, primary_key=True),
    db.Column('bookID', db.Integer, db.ForeignKey('books.id')),
    db.Column('memberID', db.Integer, db.ForeignKey('members.id')),
    db.Column("issue_date", db.DateTime(timezone=True), default=func.now(), nullable=False), 
    db.Column('status', db.Boolean, nullable=False, default=True)
)

class Books(db.Model):
    __tablename__ = 'books'
    id       = db.Column(db.Integer, primary_key=True)
    isbn     = db.Column(db.Integer, nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False)
    issued   = db.Column(db.Integer, nullable=False, default=0)
    title    = db.Column(db.String(100), nullable=False)
    author   = db.Column(db.String(100), nullable=False)
    book_id  = db.Column(db.Integer, nullable=False)
    added    = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)

    def __init__(self, book, quantity):
        self.isbn = book['isbn']
        self.quantity = quantity
        self.title = book['title']
        self.author = book['authors']
        self.book_id = book['bookID']

class Members(db.Model):
    __tablename__ = 'members'
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(100), nullable=False)
    email    = db.Column(db.String(100), nullable=False)
    credit   = db.Column(db.Integer, nullable=False)
    books = db.relationship('Books', secondary=issued, backref=db.backref('issue', lazy='dynamic'))

    def __init__(self, member):
        self.name = member['name']
        self.email = member['email']
        self.credit = member['credit']

# class Issued(db.Model):
#     __tablename__ = 'issued'
#     id       = db.Column(db.Integer, primary_key=True)
#     member_id  = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)
#     book_id  = db.Column(db.Integer, db.ForeignKey('books.book_id'), nullable=False)
#     issued = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
#     returned = db.Column(db.DateTime(timezone=True))
#     status = db.Column(db.Boolean, nullable=False, default=True)
#     rent  = db.Column(db.Integer, default=20, nullable=False)

#     def __init__(self, member, book):
#         self.member_id = member
#         self.book_id = book

# class Books(db.Model):
#     __tablename__ = 'books'
#     id       = db.Column(db.Integer, primary_key=True)
#     isbn     = db.Column(db.Integer, nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     issued   = db.Column(db.Integer, nullable=False, default=0)
#     title    = db.Column(db.String(100), nullable=False)
#     author   = db.Column(db.String(100), nullable=False)
#     book_id  = db.Column(db.Integer, unique=True)
#     added    = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)

#     def __init__(self, book, quantity):
#         self.isbn = book['isbn']
#         self.quantity = quantity
#         self.title = book['title']
#         self.author = book['authors']
#         self.book_id = book['bookID']
        
# class Members(db.Model):
#     __tablename__ = 'members'
#     id        = db.Column(db.Integer, primary_key=True)
#     name      = db.Column(db.String(100), nullable=False)
#     email     = db.Column(db.String(100), nullable=False)
#     phone     = db.Column(db.String(100), nullable=False)
#     member_id = db.Column(db.Integer, db.ForeignKey('members.id'))

# class Lms(db.Model):
#     __tablename__ = 'transactions'
#     id          = db.Column(db.Integer, primary_key=True)
#     book_id     = db.Column(db.Integer, db.ForeignKey('books'))
#     member_id   = db.Column(db.Integer, db.ForeignKey('members'))
#     date        = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
#     return_date = db.Column(db.DateTime)
#     fine        = db.Column(db.Integer)
#     status      = db.Column(db.Boolean, nullable=False)


