# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.

word = input("Please enter the word to compare first and last char: ")
list_word = list(word)

if list_word[0] == list_word[-1]:
    print(f"The first and last char are the same of the word --{word}--. "
          f"{list_word[0]} = {list_word[-1]}")
else:
    print(f"The first and last char of the --{word}-- are not the same. "
          f"{list_word[0]} not equal to {list_word[-1]}")


