# 10. Write a Python program to find the list of
# words that are longer than n from a given list of words

def find_long_words(word_list, n):
    long_words = []
    for word in word_list:
        if len(word) > n:
            long_words.append(word)
    return long_words


word_list = ['apple', 'banana', 'orange', 'pear', 'watermelon',
             'kiwi', 'strawberry']
n = 5
print(find_long_words(word_list, n))
