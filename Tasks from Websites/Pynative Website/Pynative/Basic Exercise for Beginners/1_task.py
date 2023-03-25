# Exercise 1: Calculate the multiplication and sum of two numbers

# Given two integer numbers return their product only if the product
# is equal to or lower than 1000, else return their sum

def product_solution(number1, number2):
    product = number1 * number2

    if product <= 1000:
        return print(product)
    else:
        print(number1 + number2)


number_1 = int(input("Please enter the first number: "))
number_2 = int(input("Please enter the second number: "))

product_solution(number_1, number_2)





# def sums(a, b):
#     print(f"{a} + {b} = {a + b}")
#
#
# def multiplay(a, b):
#     print(f"{a} * {b} = {a * b}")
#
#
# number1 = int(input("Please enter the first number: "))
# number2 = int(input("Please enter the second number: "))
#
#
# sums(number1, number2)
#
# multiplay(number1, number2)

