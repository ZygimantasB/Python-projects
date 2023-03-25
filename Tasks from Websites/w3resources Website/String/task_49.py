# 49. Write a Python program to count and display vowels in text.


def count_vowels(enter_string):
    count = 0
    for char in enter_string:
        if char in 'a, e, i, o, u':
            count += 1

    return f'{count}'


print(count_vowels('Write a Python program to count and display vowels in text.'))

