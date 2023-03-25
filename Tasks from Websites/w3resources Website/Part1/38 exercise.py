# 38. Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49
import math


def arithmetic_operation(a, b):
    # print((a + b) * (a + b))
    print(f"({a} + {b}) * ({a} + {b}) = {(a + b) * (a + b)}")


number1 = int(input("Please enter the number 1: "))
number2 = int(input("Please enter the number 2: "))

arithmetic_operation(number1, number2)

print(50 * "*")


print(math.pow(int(number1 + number2), 2))

print((number1 + number2) ** 2)

print(50 * "/")

x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))