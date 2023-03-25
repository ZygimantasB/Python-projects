import random
from flask import Flask

app = Flask(__name__)


def make_h1(function):
    def wrapper():
        return '<h1>' + function() + '</h1>'
    return wrapper


def show_image(image_url):
    def decorator(function):
        def wrapper():
            return f'<img src="{image_url}"> {function()}'
        return wrapper
    return decorator



@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1> <img ' \
           'src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


random_number = random.randint(0, 9)

@app.route('/<int:number>')
def guess_number(number):
    if number > random_number:
        return '<h1>The number are to low</h1>' \
    '<img src="https://media.giphy.com/media/StKiS6x698JAl9d6cx/giphy.gif"</img>'
    elif number < random_number:
        return '<h1>The number are to low </h1>' \
    '<img src="https://media.giphy.com/media/hPPx8yk3Bmqys/giphy-downsized-large.gif"</img>'
    else:
        return '<h1>You are correct</h1> ' \
               '<img src="https://media.giphy.com/media/hz6L3FwCc3hI2zUAFI/giphy.gif" </img>'



@app.route('/picture')
def picture():
    return '<img src="https://media.giphy.com/media/StKiS6x698JAl9d6cx/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)
