# 117. Write a Python program to prove that two string variables of same value point same memory location.

some_value = hex(id("hello World"))
another_value = hex(id("Hello World"))
some_value1 = hex(id("hello World"))

if some_value == some_value1:
    print(f"{some_value} = {some_value1}")
if some_value != another_value:
    print(f"{some_value} != {another_value}")
