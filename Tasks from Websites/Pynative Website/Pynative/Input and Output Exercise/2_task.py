# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
# Use the print() function to format the given words in the mentioned format.
# Display the ** separator between each string.
# Expected Output:
# For example: print('Name', 'Is', 'James') will display Name**Is**James

enter_name = input("Please enter teh name: ")
enter_surname = input("Please enter the surname: ")

print('My', 'Name', 'is', 'James', sep='**')

print(f"Your name: {enter_name} and surname: {enter_surname}", sep="**")