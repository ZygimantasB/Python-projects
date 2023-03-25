# Exercise 5: Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
#
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
# Given:
#
numbers = [12, 75, 150, 180, 145, 525, 50]

for numbers_list in numbers:
    if numbers_list > 500:
        break
    elif numbers_list > 150:
        continue
    elif numbers_list % 5 == 0:
        print(numbers_list)

for numbers_list in numbers:
    if numbers_list % 5 == 0:
        if numbers_list > 150:
            pass
            if numbers_list > 500:
                break
            print(numbers_list)
