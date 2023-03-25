# Exercise 6: Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.
#
# For example, the number is 75869, so the output should be 5.

number = 75869
count_numbers = 0

for i in str(number):
    count_numbers += 1
print(f'The number {number} has {count_numbers} digits')