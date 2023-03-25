# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
number3 = int(input("Please enter the third number: "))

three_numbers_sum = number1 + number2 + number3

if number1 == number2 == number3:
    print(three_numbers_sum * 3)
else:
    print(three_numbers_sum)


def sum_numbers(a, b, c):
    if a == b == c:
        return print((a + b + c) * 3)
    else:
        return print(a + b + c)


sum1s = int(input("Please enter the first number: "))
sum2s = int(input("Please enter the second number: "))
sum3s = int(input("Please enter the third number: "))

sum_numbers(sum1s, sum2s, sum3s)
