# Exercise 2: Print the sum of the current number and the previous number

# Write a program to iterate the first 10 numbers and in each
# iteration, print the sum of the current and previous number.

zero_value = 0

for i in range(10):
    sum_s = zero_value + i
    zero_value = i
    print(f"Current number {i} Previous number {zero_value} Sum: {sum_s}")
