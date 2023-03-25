# Exercise 4: Write a program to print multiplication table of a given number
# For example, num = 2 so the output should be
#
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

number_multiply = int(input('Please enter the number: '))
multiply_numbers = 1

for i in range(1, 11):
    print(i * number_multiply)
