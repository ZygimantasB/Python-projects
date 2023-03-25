# Exercise 1: Create a function in Python
# Write a program to create a function that takes two arguments, name and age, and print their value.

def information (name: str, number: int):
    return f'Your name is {name} and you are {number} years old'


enter_name = input('Please enter your name: ')
enter_age = int(input('Please enter your age: '))

print(information(name=enter_name, number=enter_age))