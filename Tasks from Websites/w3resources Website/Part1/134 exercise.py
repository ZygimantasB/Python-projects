# 134. Write a Python program to input two integers in a single line.

print("Input the value of x & y")
x, y = map(int, input().split())
print("The value of x & y are: ",x,y)

print("Another task")

a, b = [int(a) for a in input("Input the value of a & b: ").split()]
print("The value of a & b are:",a,b)

