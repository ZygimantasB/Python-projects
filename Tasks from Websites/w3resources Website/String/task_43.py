# 43. Write a Python program to print the square and
# cube symbols in the area of a rectangle and the volume of a
# cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
from math import pi


def area_of_the_rectangle(length, width):
    return round(length * width, 2)


def volume_cylinder_formula(radius, height):
    return pi * radius ** 2 * height


area_rectangle = 1256.66
volume_cylinder = 1254.725

print(area_of_the_rectangle(length=area_rectangle, width=volume_cylinder))

print(volume_cylinder_formula(radius=area_rectangle, height=volume_cylinder))
