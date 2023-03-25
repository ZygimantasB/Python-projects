# 133. Write a Python program to calculate the time runs
# (difference between start and current time) of a program.

from timeit import default_timer
def timer(n):
    start = default_timer()
    # some code here
    for row in range(0,n):
        print(row)
    print(default_timer() - start)

timer(5)
timer(15)
