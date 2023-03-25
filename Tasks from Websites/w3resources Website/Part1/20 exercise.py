# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def multiplay_word(word, times):
    result = ""
    for i in range(times):
        result += word
    return result


word_multiplay = input("Please write a word to multiplay: ")
number_multiplay = int(input("Please write a number, which will multiplay the word: "))

print(multiplay_word(word_multiplay, number_multiplay))
