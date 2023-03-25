class Rectangle:
    def __init__(self, length: int, width: int):
        self.length: int = length
        self.width: int = width

    def parameter(self):
        return f'Perimeter rectangle: {2 * (self.length + self.width)}'

    def area(self):
        return f'Rectangle area: {self.length * self.width}'

    def display(self):
        display_rectangle = Rectangle(self.length, self.width)
        print(display_rectangle.parameter())
        print(display_rectangle.area())


class Parallelepipede(Rectangle):
    def __init__(self, length: int, width: int, height: int):
        Rectangle.__init__(self, length, width)
        self.height: int = height

    def volume(self):
        return print(f'Parallelepipede: {self.length * self.width * self.height}')
