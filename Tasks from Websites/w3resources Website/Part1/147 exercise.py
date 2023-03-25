# 147. Write a Python function to check whether a number is
# divisible by another number. Accept two integers values form the user.

number1 = int(input("Please enter teh number 1: "))
number2 = int(input("Please enter the number 2: "))


def divisible(a, b):
    if a % b == 0:
        print("Number are divisible")
        print(True)
    else:
        print("Numbers are not divisible")
        print(False)

divisible(number1, number2)


print("\n --Another Solution -- \n")

def multiple(m, n):
    return True if m % n == 0 else False

print(multiple(20, 5))
print(multiple(7, 2))
