# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 55, 555]

for i in new_list:
    if i % 5 == 0:
        print(f"Number {i} are divisible by 5")

print("\n")

for a in new_list:
    if a % 5 != 0:
        print(f"Number {a} are not divisible by 5")