# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"

str1_lower = str1.lower()
count_usa = str1_lower.count('usa')
print(count_usa)
