# 49. Write a Python program to convert
# a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'},
# {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'},
# {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

def create_dict(list1, list2):
    return [{'color_name': key, 'color_code': value} for key, value in zip(list1, list2)]


sample_list1 = ["Black", "Red", "Maroon", "Yellow"]
sample_list2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]

print(create_dict(sample_list1, sample_list2))
