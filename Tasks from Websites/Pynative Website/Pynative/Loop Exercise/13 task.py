# Exercise 13: Find the factorial of a given number
# Write a program to use the loop to find the factorial of a given number.
#
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.
#
# For example: calculate the factorial of 5
#
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output:
#
# 120

factorial_number = 5
count_number = 1

for i in reversed(range(1, factorial_number + 1)):
    count_number *= i
    # print(i)
print(count_number)

print('\n Another Solution \n')

num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for i in range(1, num + 1):
        # multiply factorial by current number
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)