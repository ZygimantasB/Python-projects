# 3. Write a Python program to get a string made of the first 2
# and last 2 characters of a given string. If the string length is
# less than 2, return the empty string instead. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String


def check_empty_string(enter_string):
    return "Empty string" if len(enter_string) < 2 else \
        enter_string[0:2] + enter_string[-2:]


print(check_empty_string('w3resource'))
print(check_empty_string('w3'))
print(check_empty_string('w'))

