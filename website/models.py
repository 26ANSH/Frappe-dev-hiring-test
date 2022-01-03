from . import db
from sqlalchemy.sql import func, select
class Books(db.Model):
    __tablename__ = 'books'
    id       = db.Column(db.Integer, primary_key=True)
    isbn     = db.Column(db.String, nullable=False, unique=True)
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

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'     : self.id,
           'title'   : self.title,
           'isbn'  : self.isbn,
           'unique id': self.book_id,
           'quantity':self.quantity,
           'added': self.added.date()
       }

class Members(db.Model):
    __tablename__ = 'members'
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(100), nullable=False)
    email    = db.Column(db.String(100), nullable=False, unique=True)
    credit   = db.Column(db.Integer, nullable=False)
    payments = db.relationship('Payment',backref='Members', lazy='dynamic')
    books    = db.relationship('Issued',backref='Members', lazy='dynamic')
    created  = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)


    def __init__(self, member):
        self.name = member['name']
        self.email = member['email']
        self.credit = member['credit']

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'name'       : self.name,
           'email'  : self.email,
           'credit': self.credit
       }

class Issued(db.Model):
    __tablename__ = 'issued'
    id       = db.Column(db.Integer, primary_key=True)
    member_id  = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)
    book_id  = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    issued = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
    returned = db.Column(db.DateTime(timezone=True))
    status = db.Column(db.Boolean, nullable=False, default=True)
    rent  = db.Column(db.Integer, default=20, nullable=False)

    def __init__(self, member, book):
        self.member_id = member
        self.book_id = book
class Payment(db.Model):
    __tablename__ = 'payment'
    id       = db.Column(db.Integer, primary_key=True)
    member_id  = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)

    def __init__(self, id, amount):
        self.amount = amount
        member = Members.query.filter_by(id=id).first()
        member.credit = member.credit + amount
        db.session.commit()
