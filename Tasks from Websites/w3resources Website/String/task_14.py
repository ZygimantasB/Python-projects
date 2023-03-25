# 14. Write a Python program that accepts a comma-separated sequence
# of words as input and prints the distinct words in sorted form
# (alphanumerically). Go to the editor
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

def print_distinct_sorted_sentence(input_string):
    split_string = input_string.split(',')
    words = [word.strip() for word in split_string]
    result = set(sorted(words))
    return result


print(print_distinct_sorted_sentence('red, white, black, red, green, black'))


