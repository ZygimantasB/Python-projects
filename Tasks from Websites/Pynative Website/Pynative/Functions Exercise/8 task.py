# Exercise 8: Generate a Python list of all the even numbers between 4 to 30


def display_even_numbers():
    even_list = []
    for number in range(4, 30):
        if number % 2 == 0:
            even_list.append(number)
    print(even_list)

display_even_numbers()

# print(list(range(4, 30, 2)))
