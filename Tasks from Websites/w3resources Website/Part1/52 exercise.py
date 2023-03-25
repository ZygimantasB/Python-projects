# 52. Write a Python program to print to stderr.

import sys
from __future__ import print_function


def print_to_stderr(*a):
    print(*a, file=sys.stderr)


print_to_stderr("Hello Worlds")

print()

print("Example 1")
print("Example 2", file=sys.stderr)
sys.stderr.write("Example 3")


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


eprint("abc", "efg", "xyz", sep="--")
