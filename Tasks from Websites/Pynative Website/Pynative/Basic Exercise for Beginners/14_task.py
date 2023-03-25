# Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
# * * * * *
# * * * *
# * * *
# * *
# *

for a in reversed(range(0, 6)):
    for b in reversed(range(0, a)):
        print("*", end=" ")
    print(" ")

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")