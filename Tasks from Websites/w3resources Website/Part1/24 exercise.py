# 24. Write a Python program to test whether a passed letter is a vowel or not.

def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))

words = 'aeiou'

print("*" * 50)

number = input("Please enter the number: ")

if number in words:
    print(True)
else:
    print(False)
