# 4. 'builtins' module provides direct access to all 'built-in' identifiers of Python.
# Write a python program which import the abs() function using the builtins module,
# display the documentation of abs() function and find the absolute value of -155.

class ImportABS:
    def __init__(self, negative_value=-150):
        self.negative_value = negative_value

    def __str__(self):
        return f'{abs(self.negative_value)}'
