dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

print({**dict1, **dict2})
# print(dict2.update(dict1))
print(dict1 | dict2)

