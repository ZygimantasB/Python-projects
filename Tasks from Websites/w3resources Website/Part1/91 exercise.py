# 91. Write a Python program to swap two variables.

a = "a"
b = "b"

c = b
b = a
a = c

print(a)
print(b)

a = 30
b = 20
print("\nBefore swap a = %d and b = %d" %(a, b))
a, b = b, a
print("\nAfter swaping a = %d and b = %d" %(a, b))
print()

x = 34
y = 56
print("Initial Value of x =", x)
print("Initial Value of y =", y)
temp = x
x = y
y = temp
print("\nAfter swaping value of x =", x)
print("After swaping value of y =", y)
