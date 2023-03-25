# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age)
# to it and call it using the new name.

def display_student(name, age):
    print(name, age)

def show_student(name='James', age=17):
    print(name, age)


show_students = display_student("Emma", 26)
