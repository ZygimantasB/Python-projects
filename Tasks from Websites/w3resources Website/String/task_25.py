# 25. Write a Python program to create a Caesar encryption.
#
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher,
# the shift cipher, Caesar's code or Caesar shift, is one of the simplest
# and most widely known encryption techniques. It is a type of substitution
# cipher in which each letter in the plaintext is replaced by a letter some fixed
# number of positions down the alphabet. For example, with a left shift of 3, D would
# be replaced by A, E would become B, and so on. The method is named after Julius
# Caesar, who used it in his private correspondence.

def caesar_cipher(user_password: str, shift: int):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    user_password = user_password.lower()
    encrypted_text = ''
    for char in user_password:
        if char in alphabet:
            char_index = alphabet.index(char)
            encrypted_text += shifted_alphabet[char_index]
        else:
            encrypted_text += char
    return encrypted_text


print(caesar_cipher(user_password='cryptography', shift=3))
