# 68. Write a Python program to calculate sum of digits of a number.

number1 = input("Please enter digit numbers: ")

list_number = list(number1)

new_number = 0

for i in list_number:
    new_number += int(i)

print(f"The sum of {number1} are {new_number}")

sum = int(number1[0]) + int(number1[1]) + int(number1[2]) + int(number1[3])

print(sum)

num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)


