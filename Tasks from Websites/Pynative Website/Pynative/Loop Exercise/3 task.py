# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
#
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
#
# Expected Output:
#
# Enter number 10
# Sum is:  55

giver_number = int(input('Please enter the number: '))

sum_numbers = 0

for i in range(giver_number +1):
    sum_numbers += i
print(sum_numbers)