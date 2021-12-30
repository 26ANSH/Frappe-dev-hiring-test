from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import requests
from .models import *
import json
from . import db


member = Blueprint('members', __name__)

@member.route('/')
def index():
    if "logged_in" in session:
        # id = 2
        # member = Members.query.get(id)
        # member.payments.append(Payment(id, 1000))
        # db.session.commit()
        return render_template('members/index.html', users=Members.query.all())
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

@member.route('/transactions')
def transactions():
    if "logged_in" in session:
        books= [str(book.id) for book in Books.query.with_entities(Books.id)]
        # print(books)
        return render_template('members/transactions.html', transactions=Issued.query.all(),  books = books)
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
            new = {
                'name': request.form['name'],
                'email': request.form['email'],
                'credit': request.form['credit']
            }
            new_member = Members(new)
            print(new_member)
            db.session.add(new_member)
            db.session.commit()
            return render_template('members/newuser.html', user = new_member)

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