# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def sum_values(a, b, c):
    if a == b or a == c or b == c:
        return print("Value: " + "0")
    else:
        return sum == a + b + c



# def sum_values1(a, b, c):
#     if a == b or a == c or b == c:
#         sum = 0
#     else:
#         sum = a + b + c
#     return sum

number1 = int(input("Please enter the number 1: "))
number2 = int(input("Please enter the number 2: "))
number3 = int(input("Please enter the number 3: "))

sum = number1 + number2 + number3

if number1 == number2 or number1 == number3 or number2 == number3:
    print(f"Number1: {number1} - Number2: {number2} - Number3: {number3}")
    print("all three numbers sum are equal")
else:
    print(f"{number1} + {number2} + {number3} = {sum}")

print(50 * '-')

print(sum_values(number1, number2, number3))

print(50 * '-')


def sum_three(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum
print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))


