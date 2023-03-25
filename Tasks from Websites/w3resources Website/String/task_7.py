# 7. Write a Python program to find the first appearance
# f the substrings 'not' and 'poor' in a given string. If
# 'not' follows 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def changing_string(string1):
    search_word_poor = string1.split(' ')
    for _ in search_word_poor:
        if 'poor!' in search_word_poor:
            return 'The lyrics is not that good!'
    else:
        return 'The lyrics is not that poor!'


check_string = 'The lyrics is not that poor!'

print(changing_string(check_string))


def change_string1(string):
    not_index = string.find("not")
    poor_index = string.find("poor")
    if not_index < poor_index:
        string = string[:not_index] + "good" + string[poor_index+4:]
    return string


print(change_string1("The lyrics is not that poor!"))
print(change_string1("The lyrics is poor!"))
