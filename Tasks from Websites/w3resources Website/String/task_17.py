# 17. Write a Python function to get a string made of 4 copies of
# the last two characters of a specified string (length must be at
# least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

def multiply_last_chars(input_words):
    return input_words[-2:] * 4


print(multiply_last_chars('Python'))
print(multiply_last_chars('Exercises'))
