# 12. Write a Python program to count the
# occurrences of each word in a given sentence.

def count_words(sentence):
    words_counter_dict = {}
    split_words = sentence.split()
    for word in split_words:
        if word in words_counter_dict:
            words_counter_dict[word] += 1
        else:
            words_counter_dict[word] = 1
    return words_counter_dict


print(count_words('The the the cat cat cat jumped over '
                  'the the the fence fence fence.'))