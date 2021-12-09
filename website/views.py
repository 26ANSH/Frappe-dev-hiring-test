from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import requests
from .models import Books
from . import db
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
                print(request.args.get('error'))
                return render_template("login.html", error=request.args.get('error'))
            elif request.args.get('alert'):
                print(request.args.get('alert'))
                return render_template("login.html", alert=request.args.get('alert'))
            else:
                return render_template("login.html")
        else:
            session['first_name'] = request.form['fname']
            session['last_name'] = request.form['lname']
            session['logged_in'] = True

            return redirect(url_for('views.dashboard'))

@views.route('/settings', methods=['GET', 'POST'])
def profile():
    if "logged_in" in session:
        if request.method == 'GET':
            for book in Books.query.all():
                print(book.title)

            return render_template("settings.html")
        else:
            session['first_name'] = request.form['fname']
            session['last_name'] = request.form['lname']
            return render_template("settings.html", alert="Settings Updated !!!")
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

@views.route('/dashboard', methods=['GET'])
def dashboard():
    if "logged_in" in session:
        return render_template("dashboard.html")
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

@views.route('/browse', methods=['GET'])
def browse():
    return render_template("browse.html")

@views.route('/logout', methods=['GET'])
def logout():
    if "logged_in" in session:
        session.clear()
        return redirect(url_for('views.index', alert="Logged out Successfully."))