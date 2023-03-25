# 124. Write a Python program to check whether multiple variables have the same value.

def multiple_variables_equality(*vars):
    for x in vars:
        if x != vars[0]:
            return "All variables have not same value."
    return "All variables have same value."
print(multiple_variables_equality(2,3,2,2,2,2))
print(multiple_variables_equality(10,10,10,10))
print(multiple_variables_equality(-3,-3,-3,-3))

x = 20
y = 20
z = 20
if x == y == z == 20:
    print("All variables have same value!")

