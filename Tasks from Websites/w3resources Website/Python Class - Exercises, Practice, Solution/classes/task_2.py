# 2. Write a Python program to create a class and display the namespace of the said class.

class PrintNamespace:
    def __init__(self, my_name = 'James', my_age=19):
        self.my_name = my_name
        self.my_age = my_age

    def __str__(self):
        return f"{self.my_name} {self.my_age}"
