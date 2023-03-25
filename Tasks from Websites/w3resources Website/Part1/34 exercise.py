# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def sum_two_numbers(a, b):
    if sum in range(15, 20):
        return print(20)
    else:
        return print(a + b)


number1 = int(input("Please enter the number1: "))
number2 = int(input("Please enter the number2: "))

# sum = number1 + number2


if sum in range(15, 21):
    print(20)
else:
    print(f"{number1} + {number2} = {sum}")

print(50 * "/")

sum_two_numbers(number1, number2)

print(50 * "/")


def sum1(x, y):
    sum1 = x + y
    if sum1 in range(15, 20):
        return 20
    else:
        return sum

print(sum1(10, 6))
print(sum1(10, 2))
print(sum1(10, 12))
