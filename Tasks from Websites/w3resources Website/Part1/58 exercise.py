# 58. Write a Python program to sum of the first n positive integers.

n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", sum_num)

result = sum(range(n + 1))

print(result)

