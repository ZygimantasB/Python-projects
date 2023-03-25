# 6. Write a Python program to add 'ing' at the end of a given string
# (length should be at least 3). If the given string already ends with
# 'ing', add 'ly' instead. If the string length of the given string
# is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def combined_string(string1):
    if string1[-3:] == 'ing':
        return string1 + 'ly'
    elif len(string1) >= 3:
        return string1 + 'ing'
    else:
        return string1


print(combined_string('ab'))
print(combined_string('abc'))
print(combined_string('abcing'))
