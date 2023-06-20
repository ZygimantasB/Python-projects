from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, SelectMultipleField, SelectField
from flask_migrate import migrate
from wtforms.validators import DataRequired

from .models import Author, Publisher


class BookForm(FlaskForm):
    title = StringField('title', [DataRequired()])
    description = StringField('description', [DataRequired()])
    price = DecimalField('price', [DataRequired()])
    quantity = IntegerField('quantity', [DataRequired()])
    publisher = SelectField('publisher', [DataRequired()])

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.publisher.choices = [(publisher.id, publisher.name) for publisher in Publisher.query.all()]


class AuthorForm(FlaskForm):
    name = StringField('name', [DataRequired()])
    surname = StringField('surname', [DataRequired()])
    phone_number = IntegerField('phone_number', [DataRequired()])


class PublisherForm(FlaskForm):
    name = StringField('name', [DataRequired()])
