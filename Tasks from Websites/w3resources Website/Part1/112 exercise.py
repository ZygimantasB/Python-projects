# 112. Write a Python program to remove the first item from a specified list.

new_list = [0, 1, 2, 3, 4, 5, 6]

new_list.remove(0)

print(new_list)

for i in new_list:
    print(i)

print("1 solution")

color = ["Red", "Black", "Green", "White", "Orange"]
print("Original list elements:")
print(color)
del color[0]
print("After removing the first color:")
print(color)

print("2 solution")

color = ["Red", "Black", "Green", "White", "Orange"]
print("Original list elements:")
print(color)
print("\nAfter removing the first element from the said list:")
new_color = color[1:]
print(new_color)