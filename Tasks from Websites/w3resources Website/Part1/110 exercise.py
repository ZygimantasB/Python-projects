# 110. Write a Python program to get numbers divisible
# by fifteen from a list using an anonymous function.

# for i in divisible_list:
#     if i % 15 == 0:
#         print(i, end="-")
#     # if i % 7 == 0:
#     #     print(i, end=", ")


another_list = [7, 98, 6358, 41258, 6954, 2314, 3258, 6547, 6987, 4102]

new_lambda = list(filter(lambda y: (y % 7 ==0), another_list))
print(new_lambda)

second_list = [78, 98, 52, 45, 69, 687, 456, 123, 789, 456, 789, 9654, 789432]

list_range = range(0, 100)

number_list = list(filter(lambda a: (a % 15 == 0), list_range))
print(number_list)