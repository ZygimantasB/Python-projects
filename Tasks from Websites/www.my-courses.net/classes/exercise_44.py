import math


class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def area(self):
        return math.pi * math.pow(self.r, 2)

    def perimeter(self):
        return 2 * math.pi * self.r

    def form_equation(self, x, y):
        return (x-self.a)**2 + (y-self.b)**2 * self.r**2

    def test_belongs(self, x ,y):
        if self.form_equation(x, y) == 0:
            print('the point:(", x, y,") belongs to the circle')
        else:
            print('The point: (", x, y,") does not belong to the circle')

