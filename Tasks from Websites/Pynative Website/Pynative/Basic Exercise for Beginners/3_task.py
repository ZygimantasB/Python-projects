# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.
#
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

# str = "pynative"
str = "labas"

enumerate_value = [enum_value for index, enum_value in enumerate(str) if index % 2 == 0]
print(enumerate_value)

for a in enumerate_value:
    print(a)

print("\n--Below try--\n")

value_2 = str[0::2]

for i in value_2:
    print(i)

print("\n--Below try--\n")

word_even = input("Please enter the word: ")
print(f"Original value {word_even}")

for i in range(0, len(word_even), 2):
    print(f"The index of {i} are {word_even[i]}")