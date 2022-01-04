from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from .models import *
from . import db, PASSWORD

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
        return render_template("main/dashboard.html", books = Books.query.count(), members = Members.query.count())
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

@views.route('/logout', methods=['GET'])
def logout():
    if "logged_in" in session:
        session.clear()
        return redirect(url_for('views.index', alert="Logged out Successfully."))
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))
