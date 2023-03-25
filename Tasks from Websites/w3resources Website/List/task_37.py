# 37. Write a Python program to find common items in two lists.

def common_items(list1, list2):
    return [number1 for number1 in list1
            for number2 in list2 if number1 == number2]


sample_list1 = [1, 2, 3, 4, 5]
sample_list2 = [6, 7, 8, 9, 5]

color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"

print(common_items(sample_list1, sample_list2))
print(common_items(color1, color2))
