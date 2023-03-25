# 28. Write a Python program to add prefix text to all of the lines in a string.

import textwrap
sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
text_without_Indentation = textwrap.indent(sample_text, '>')
print()
print(text_without_Indentation)
print()