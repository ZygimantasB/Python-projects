# 37. Write a Python program to display your details like name, age, address in three different lines.


name = input("Please enter the name: ")
age = int(input("Please enter your age: "))
adress = input("Please enter your adress: ")

print(f"- Your name is {name},\n- your age is {age} \n- and you live in {adress}")

print("*" * 50)

print("Your name" + name)
print("Your age is " + str(age))
print("Your adress is " + adress)

print("*" * 50)

print(f"""Your name is {name}
Your age is {age}
Your adress is {adress}""")

print("My info")


def your_inormation(a, b, c):
    print("Your name is " + a)
    print("Your age is " + str(b))
    print("Your adress is " + c)


your_inormation(name, age, adress)


def personal_details():
    name1, age1 = "Simon", 19
    address1 = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name1, age1, address1))


personal_details()
