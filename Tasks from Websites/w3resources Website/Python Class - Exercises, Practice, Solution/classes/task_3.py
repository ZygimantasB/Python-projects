# 3. Write a Python program to create an instance of a specified class and display the namespace of the said instance.

class CreateNamespace:
    def __init__(self, my_name, my_age, my_place):
        self.my_name = my_name
        self.my_age = my_age
        self.my_place = my_place

    def __str__(self):
        return f'{self.my_name} {self.my_age} {self.my_place}'
