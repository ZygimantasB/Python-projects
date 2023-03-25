class Book:
    def __init__(self, title: str = 'Lord of the Rings', author: str = 'J. R. R. Tolkien', price: float = 19.99):
        self.title = title
        self.author = author
        self.price = price

    def view(self):
        return f'Book title: {self.title},\n' \
               f'Book author: {self.author},\n' \
               f'Book price: {self.price} $'
