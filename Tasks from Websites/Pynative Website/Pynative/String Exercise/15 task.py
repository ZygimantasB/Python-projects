# Exercise 15: Remove special symbols / punctuation from a string
# Given:
# str1 = "/*Jon is @developer & musician"
# Expected Output:
# "Jon is developer musician"
import string, re

str1 = "/*Jon is @developer & musician"

# new_value = str1.translate(str.maketrans('', '', string.punctuation))
# print(new_value)

res = re.sub(r'[^\w\s]', '', str1)
print(res)
