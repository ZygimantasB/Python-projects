# 51. Write a Python program to determine profiling of Python programs. Go to the editor
# Note: A profile is a set of statistics that describes how often and for how long various parts
# of the program executed. These statistics can be formatted into reports via the pstats module.

import pstats
import cProfile

print(pstats.Stats)
print(pstats.StatsProfile)


def sum(a, b):
    print(a + b * a / b * a + a / a)


a = float(input("Please enter teh number 1: "))
b = float(input("Please enter the number 2: "))


cProfile.run('sum(a, b)')
print(sum(a, b))
