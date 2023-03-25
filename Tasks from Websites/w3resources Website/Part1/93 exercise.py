# 93. Write a Python program to get the Identity, Type, and Value of an object.

a = 20
b = "string"
c = "a"
d = 22.22

print(type(a))
print(id(a))
print(type(b))
print(id(b))
print(type(c))
print(id(c))
print(type(d))
print(id(d))

#Define two variables with some values
a = 34
b = 33
print('a = ',a)
print('b = ',b)
#Define another vairable c which is equal to a
c = a
print("Compare a and b:")
print(a is b)
print("\nMemory address of a:")
print(id(a))
print("Memory address of b:")
print(id(b))
print("\nCompare the said memory address:")
print(id(a) == id(b))
print("\nCompare b and c:")
print(b is c)
print("Memory address of c:")
print(id(c))

x = 34
print("\nIdentity: ",x)
print("\nType: ",type(x))
print("\nValue: ",id(x))
