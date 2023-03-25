# Exercise 14: Remove empty strings from a list of strings
# Given:
#
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# Expected Output:
#
# Original list of sting
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
#
# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# filtered_list = list(filter(None, str_list))
# print(filtered_list)

append_non_empty = []

for i in str_list:
    if i:
        append_non_empty.append(i)
print(append_non_empty)
