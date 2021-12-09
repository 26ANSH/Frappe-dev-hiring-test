from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import requests
import json
from .models import Books
from . import db

URL = "https://frappe.io/api/method/frappe-library/?page="
api = Blueprint('api', __name__)

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

@api.post('/get_books')
def get_books():
    params = json.loads(request.data)

    if params['title'] != '' and params['authors'] != '':
        bookByTitle = requests.get(URL+f"{params['page']}&title={params['title']}").json()['message']
        bookByAuthors = requests.get(URL+f"{params['page']}&authors={params['authors']}").json()['message']
        books = intersection(bookByTitle, bookByAuthors)
    elif params['title'] != '':
        books = requests.get(URL+f"{params['page']}&title={params['title']}").json()['message']
    elif params['authors'] != '':
        books = requests.get(URL+f"{params['page']}&authors={params['authors']}").json()['message']
    else:
        books = requests.get(URL+f"{params['page']}").json()['message']

    return jsonify(books)
