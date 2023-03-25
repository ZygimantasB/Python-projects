# 16. Write a Python function to insert a string in
# the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

# Not my solution

def insert_string_middle(original, insertion):
    mid = len(original) // 2
    if len(original) % 2 == 0:
        return original[:mid-1] + insertion + original[mid+1:]
    else:
        return original[:mid] + insertion + original[mid+1:]


print(insert_string_middle('[[]]<<>>', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))

