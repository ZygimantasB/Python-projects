# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.
#
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
# See: Default arguments in function
#
# Given:
#
# showEmployee("Ben", 12000)
# showEmployee("Jessa")

def showEmployee(name: str, salary: int = 9000):
    print(f'Name: {name} salary {salary}')


showEmployee("Ben", 12000)
showEmployee("Jessa")
