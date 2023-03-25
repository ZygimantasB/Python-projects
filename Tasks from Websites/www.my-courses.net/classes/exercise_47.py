import math


class Geometry:
    def __init__(self):
        pass

    def distance(self):
        distance_1 = [12, 78]
        distance_2 = [42, 23]

        counting = math.sqrt(((distance_1[0] - distance_2[0]) ** 2) +
                             (distance_1[1] - distance_2[1]) ** 2)
        print('%.2f' % counting)

    def middle(self):
        distance_1 = [12, 78]
        distance_2 = [42, 23]

        midpoint_distance = (distance_1[0] + distance_2[0]) / 2, \
            (distance_1[1] + distance_2[1]) / 2
        print(f'Midpoint distance: {midpoint_distance}')

    def triangle_perimeter(self, a: int = 5, b: int = 7, c: int = 9):
        print(f'Triangle perimeter: {a + b + c}')

    def triangle_isoscel(self, a: int = 7, b: int = 8, c: int = 9):
        if a == b or b == c or a == c:
            result = True
        else:
            result = False
        print(result)
