# 36. Write a Python program to add two objects if both objects are an integer type.

number1 = input("Please enter the number: ")
number2 = int(input("Please enter the number: "))

# if isinstance(number, int):
#     print("Whis is a number")
# else:
#     print("Whis is not a number")
#
#
# if not isinstance(number, int):
#     print("Please enter the number")
# else:
#     print("You entered a number")


def check_object_int(a):
    if not isinstance(a, int):
        return print("This is not a intiger !")
    elif isinstance(a, int):
        return print(a ** a)


check_object_int(number1)
check_object_int(number2)

print(50 * "*")

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Inputs must be integers!"
    return a + b


print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))
