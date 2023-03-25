keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# print(dict(zip(keys, values)))

print({keys[i]: values[i] for i in range(len(keys))})

print(dict(map(lambda x, y: (x, y), keys, values)))
