# Exercise 15: Write a function called exponent(base, exp) that returns
# an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)







