# # Exercise 8: Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# # 5 5 5 5 5

for i in range(6):
    for a in range(i):
        print(i, end=" ")
    print("\n")