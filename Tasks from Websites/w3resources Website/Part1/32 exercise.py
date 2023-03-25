# 32. Write a Python program to get the least common multiple (LCM) of two positive integers.

def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y
    while(True):
        if((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1
    return lcm
print(lcm(4, 6))
print(lcm(15, 17))

print(50 * "-")

from functools import reduce
from math import gcd

def lcm(numbers):
    return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)

print(lcm([12, 7]))
print(lcm([1, 3, 4, 5]))
print(lcm([4, 6]))
print(lcm([15, 17]))

print(50 * "-")

from fractions import gcd
def lcm(a, b):
    return (a * b) // gcd(a,b)
print(lcm(4, 6))
print(lcm(15, 17))
