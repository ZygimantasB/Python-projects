# 26. Write a Python program to display formatted text (width=50) as output

def display_formatted_text(user_input, width):
    return width * ' ' + user_input


print(display_formatted_text(user_input='Google', width=50))

import textwrap

sample_text = '''
Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java.
'''
print()
print(textwrap.fill(sample_text, width=50))
print()

