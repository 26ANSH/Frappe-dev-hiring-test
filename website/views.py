from flask import Blueprint, render_template, request, redirect, url_for, session
import requests

views = Blueprint('views', __name__)

def page_not_found(e):
    return render_template('404.html'), 404

@views.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if request.args.get('error') != '':
            return render_template("login.html", error=request.args.get('error'))

        return render_template("login.html")
    else:
        session['first_name'] = request.form['fname']
        session['last_name'] = request.form['lname']
        session['logged_in'] = True

        return redirect(url_for('views.dashboard'))


@views.route('/dashboard', methods=['GET'])
def dashboard():
    if "logged_in" in session:
        books = requests.get(f'https://frappe.io/api/method/frappe-library').json()['message']
        return render_template("dashboard.html", books=books)
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

@views.route('/logout', methods=['GET'])
def logout():
    if "logged_in" in session:
        session.clear()
        return redirect(url_for('views.index'))