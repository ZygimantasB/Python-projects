# class Employee:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#
# e = Employee('LeBron', 'James')
# print(e.get_full_name())



# def get_full_name(employee):
#     return f'{employee["first_name"]} {employee["last_name"]}'
#
#
# def create_employee(first_name, last_name, get_full_name_function):
#     enter_credentials = {'first_name': first_name, 'last_name': last_name, 'get_full_name': get_full_name_function}
#     return enter_credentials
#
#
# enter_name_lastname = create_employee('LeBron', 'James', get_full_name)
# print(enter_name_lastname['get_full_name'](enter_name_lastname))

print('\n With self \n')


def get_full_name(self):
    return f'{self["first_name"]} {self["last_name"]}'


def create_employee(first_name, last_name, get_full_name_function):
    enter_credentials = {'first_name': first_name, 'last_name': last_name, 'get_full_name': get_full_name_function}
    return enter_credentials


enter_name_lastname = create_employee('LeBron', 'James', get_full_name)
print(enter_name_lastname['get_full_name'](enter_name_lastname))
