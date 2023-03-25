class Person:
    def __init__(self, name: str, age: str):
        self.name: str = name
        self.age: str = age

    def display(self):
        return print(f'Person name: {self.name} and age: {self.age}')


class Student(Person):
    def __init__(self, name: str, age: str):
        Person.__init__(self, name, age)

    def display_student(self):
        return print(f'Student name: {self.name} and age: {self.age}')
