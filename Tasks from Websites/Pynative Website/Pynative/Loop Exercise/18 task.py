# # Exercise 18: Print the following pattern
# # Write a program to print the following start pattern using the for loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


for i in range(0, 6):
    for j in range(1):
        i *= '* '
        print(i)
for a in range(6, 0, -1):
    for b in range(1):
        a *= '* '
        print(a)

print('\n Another Solution \n')

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")