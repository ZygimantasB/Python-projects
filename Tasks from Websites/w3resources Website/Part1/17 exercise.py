# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

# def near_thousand(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))
# print(near_thousand(2200))


check_value = int(input("Please enter teh value: "))

while True:
    print(abs(1000 - check_value) <= 100) or (abs(2000 - check_value) <= 100)

    check_value = int(input("Please enter teh value: "))