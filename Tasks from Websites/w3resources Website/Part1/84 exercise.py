# 84. Write a Python program to count the number occurrence of a specific character in a string.

string = "Hellos ins tos ts"

increment_value = 0


for i in string:
    if "s" in i:
        increment_value += 1
print(increment_value)

count_count = string.count("s")
print(count_count)


s = "The quick brown fox jumps over the lazy dog."
print("Original string:")
print(s)
print("Number of occurrence of 'o' in the said string:")
print(s.count("o"))
