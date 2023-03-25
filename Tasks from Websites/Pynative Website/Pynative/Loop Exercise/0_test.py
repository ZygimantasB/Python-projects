
print('apple\rorange')
print('apple\torange')


new_value = 'Hello world'

try_slicing1 = slice(len(new_value) // 2, len(new_value))
try_slicing2 = slice(0, len(new_value) // 2)


print(new_value[try_slicing1] + new_value[try_slicing2])
# print(new_value[try_slicing2] + new_value[try_slicing1])
