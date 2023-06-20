from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import BookForm
from .models import Books, Publisher
from flask_login import login_required
from . import app, db

books = Blueprint('books', __name__)


@books.route('/insert_books', methods=['POST', 'GET'])
@login_required
def insert_books():
    books_form = BookForm()

    if books_form.validate_on_submit():
        title = books_form.title.data
        description = books_form.description.data
        price = books_form.price.data
        quantity = books_form.quantity.data
        publisher_id = books_form.publisher.data

        publisher = Publisher.query.filter_by(id=publisher_id).first()

        if publisher:
            new_book = Books(title=title,
                             description=description,
                             price=price,
                             quantity=quantity,
                             publisher_id=publisher_id)

            db.session.add(new_book)
            db.session.commit()

            return render_template('book_added.html', books_form=books_form)

    return render_template('insert_books.html', books_form=books_form)


@books.route('/show_books')
def show_books():
    books = Books.query.all()
    return render_template('show_books.html', books=books)
