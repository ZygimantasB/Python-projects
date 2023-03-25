# 5. Write a Python program which accepts the user's first and last name and
# print them in reverse order with a space between them.

name = input("Please enter your name: ")
surname = input("Please enter your surname: ")

fullname = f"{surname} {name}"
fullname1 = surname + " " + name
print(fullname)
print(fullname1)

print("%s %s" % (surname, name))