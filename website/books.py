from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import requests
from .models import Books
import json
from . import db

URL = "https://frappe.io/api/method/frappe-library/?page="
books = Blueprint('books', __name__)

@books.route('/')
def index():
    books = Books.query.all()
    return render_template('books/index.html', books= books)

@books.route('/book/<int:id>')
def book(id):
    book = Books.query.filter_by(book_id=id).first()
    return render_template('books/book.html', book=book)

@books.route('/import', methods=['GET'])
def dashboard():
    if "logged_in" in session:
        return render_template("books/import.html")
    else:
        return redirect(url_for('views.index', error="Please login to view this page."))

# API stuff #
@books.delete('/delete-book')
def ok():
    params = json.loads(request.data)
    id = int(params['id'])
    print('Delete request received for book id = ',id)
    check = Books.query.filter_by(id=id).delete()
    db.session.commit()
    print(check)
    return jsonify({'success': True})

@books.post('/add-books')
def add():
    params = json.loads(request.data)
    print(type(params))

    url = ''

    if 'title' in params:
        url = url + '&title=' + params['title']
    
    if 'author' in params:
        url = url + '&authors=' + params['author']

    if 'publisher' in params:
        url = url + '&publisher=' + params['publisher']
        
    quantity = int(params['quantity'])
    perbook = int(params['perbook'])
    page = 1
    while quantity > 0:
        response = requests.get(URL + str(page) + url).json()['message']
        if len(response) == 0:
            break
        for book in response:
            if quantity == 0:
                break
            if len(Books.query.filter_by(book_id=book['bookID']).all()) == 0:
                new = Books(book, perbook)
                db.session.add(new)
                quantity -= 1
        page += 1
    db.session.commit()
    
    return jsonify({'added': int(params['quantity']) - quantity})