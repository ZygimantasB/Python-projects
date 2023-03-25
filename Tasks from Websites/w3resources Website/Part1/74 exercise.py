# 74. Write a Python program to hash a word.

import hashlib

word = "Hello World"

hash_word = hash(word)
# hash_word1 = str(hash(word))
hash_words = hashlib.md5(b"trying to hash MD 5 and write hello world")
new_hash = hashlib.md5(word.encode())


print(hash_word)
print(hash_words)
print(new_hash.hexdigest())

soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]

word=input("Input the word be hashed: ")

word=word.upper()

coded=word[0]

for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])
print()
print("The coded word is: "+coded)
print()
