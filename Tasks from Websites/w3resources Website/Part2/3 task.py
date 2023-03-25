# 3. Write a Python program to remove and print every third
# number from a list of numbers until the list becomes empty.

new_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

new_list_value = [item for index, item in enumerate(new_list) if index % 3 != 0]
print(new_list_value)

for i in enumerate(new_list):
    print(i)


def remove_nums(int_list):
    #list starts with 0 index
    position = 3 - 1
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (position+idx) % len_list
        print(int_list.pop(idx))
        len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)
