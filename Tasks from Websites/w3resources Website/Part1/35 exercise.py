# 35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5

def try_some_values(a, b):
    if a == b or abs(a - b) == 5 or a + b == 5:
        return print(True)
    else:
        return print(False)


number1 = int(input("Please enter the number 1: "))
number2 = int(input("Please enter the number 2: "))

if number1 == number2 or abs(number1 - number2) == 5 or number1 + number2 == 5:
    print(True)
else:
    print(f"{number1} + {number2} = {number1 + number2}")
    print(False)

print(50 * "/")

try_some_values(number1, number2)

# new task TODO
print(50 * "/")


def test_number5(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False
print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
print(test_number5(27, 53))
