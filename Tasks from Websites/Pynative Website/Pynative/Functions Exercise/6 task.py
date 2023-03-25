# Exercise 6: Create a recursive function
# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
#
# A recursive function is a function that calls itself again and again.
#
# Expected Output:

def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0


res = addition(10)
print(res)