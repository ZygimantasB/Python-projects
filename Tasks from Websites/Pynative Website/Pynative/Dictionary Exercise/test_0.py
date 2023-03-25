from collections import ChainMap

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)
# print(dict1)
# new_dict = {**dict1, **dict2}
# print(new_dict)
# print(dict1 | dict2)

merged_dict = ChainMap(dict1, dict2)

print(merged_dict)

