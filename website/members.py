from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import requests
from .models import *
import json
from . import db
import datetime


member = Blueprint('members', __name__)

def issue(member, book, status):
    Book = Books.query.get(book)
    Member = Members.query.get(member)

    if Book is None:
            return 400, "Book not found"
    elif Book.quantity - Book.issued <= 0:
            return 400, "Book not available"


    if Member is None:
        return 400, "Member not found"
    
    issued = Issued.query.filter_by(member_id=member, book_id=book, status=True).first()
    
    if status == True:
        if issued:
            return 400, 'Book Already Issued'
        else:
            issued = Issued(member, book)
            Member.credit = Member.credit - 20
            Member.books.append(issued)
            db.session.commit()
            return 200, 'Book Issued'
    else:
        if not issued:
            return 400, 'Book not Issued'
        else:
            issued.returned = datetime.datetime.now()
            issued.status = False
            db.session.commit()
            return 200, 'Book Returned'

@member.route('/')
def index():
    if "logged_in" in session:
        return render_template('members/index.html', users=Members.query.all())
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

@member.route('/transactions')
def transactions():
    if "logged_in" in session:
        # books= [str(book.id) for book in Books.query.with_entities(Books.id)] 
        if request.method == 'GET':
            return render_template('members/transactions.html', transactions=Issued.query.all())
        else:
            params = json.loads(request.data)
            member_id = params['member_id']
            book_code = params['book_code']
            status = params['status']
            code, msg = issue(member_id, book_code, status)
            return jsonify(msg=msg, code=code), code
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

@member.get('/member/<int:id>')
def get(id):
    if "logged_in" in session:
        user = Members.query.get(id)
        if user is None:
            return jsonify(error="User not found"), 404
        else:
            return jsonify(user=user.serialize), 200
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

@member.route('/payments')
def payments():
    if "logged_in" in session:
        return render_template('members/payments.html', payments=Payment.query.all())
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

@member.route('/add', methods=['GET', 'POST'])
def newUser():
    if "logged_in" in session:
        if request.method == 'POST':
            params = json.loads(request.data)
            new = {
            'name':params['name'],
            'email':params['email'],
            'credit':0
            }    
            try:
                new_member = Members(new)
                db.session.add(new_member)
                db.session.commit()
                member = Members.query.get(new_member.id)
                member.payments.append(Payment(new_member.id, int(params['credit'])))
                db.session.commit()
                return jsonify(user=member.serialize, result=200), 200
            except:
                return jsonify(result="User Email '{}' already Exists".format(new['email'])), 200
        else:
            return render_template('members/newuser.html')
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

# @views.route('/member')
# def member():
#     member = {
#         'name':'Ansh Vidyabhanu',
#         'email':'anshvidyabhanu8@gmail.com',
#         'credit':100
#     }
#     member = Members(member)
#     db.session.add(member)
#     db.session.commit()
#     member = Members.query.get(1)
#     for i in range(1,3):
#         member.books.append(Books.query.get(i))
#     db.session.commit()
#     return jsonify({'Member Created':member.id})


# @views.route('/issue')
# def issue():
#     member = Members.query.get(1)
#     return jsonify({'books': len(member.books)})

# @views.route('/issues')
# def issues():
#     isues = db.session.execute(select(issued)).all()
#     all_issues = {'done':'ok'}
#     for issue in isues:
#         print(issue.memberID,"=",issue.bookID,"Status =",issue.status)
#     return jsonify({'books': all_issues})