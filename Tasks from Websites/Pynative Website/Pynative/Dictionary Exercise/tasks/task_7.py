sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict.values():
    print("200 present in a dict")
else:
    print('No')

print(200 if 200 in sample_dict.values() else 'Value is not in the list')
