from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import requests
from .models import *
from . import db, PASSWORD
import json

views = Blueprint('views', __name__)

def page_not_found(e):
    return render_template('404.html'), 404

@views.route('/', methods=['GET', 'POST'])
def index():
    if "logged_in" in session:
        return redirect(url_for('views.dashboard'))
    else:
        if request.method == 'GET':
            if request.args.get('error'):
                return render_template("main/login.html", error=request.args.get('error'))
            elif request.args.get('alert'):
                return render_template("main/login.html", alert=request.args.get('alert'))
            else:
                return render_template("main/login.html")
        else:
            pswd = request.form['pswd']
            if pswd == PASSWORD:
                session['first_name'] = request.form['fname'].capitalize() 
                session['last_name'] = request.form['lname'].capitalize() 
                session['logged_in'] = True
                return redirect(url_for('views.dashboard'))
            else:
                return redirect(url_for('views.index', error="Incorrect Password"))

@views.route('/settings', methods=['GET', 'POST'])
def profile():
    if "logged_in" in session:
        if request.method == 'GET':
            return render_template("main/settings.html")
        else:
            session['first_name'] = request.form['fname']
            session['last_name'] = request.form['lname']
            return render_template("main/settings.html", alert="Settings Updated !!!")
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

@views.route('/dashboard', methods=['GET'])
def dashboard():
    if "logged_in" in session:
        return render_template("main/dashboard.html")
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

@views.route('/logout', methods=['GET'])
def logout():
    if "logged_in" in session:
        session.clear()
        return redirect(url_for('views.index', alert="Logged out Successfully."))

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