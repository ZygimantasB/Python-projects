# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

print(50 * "-")

def gcd(x, y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))


print(50 * "-")


def gcd(x, y):
    z = x % y
    while z:
        x = y
        y = z
        z = x % y
    return y
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))


print(50 * "-")


from functools import reduce
from math import gcd as _gcd
def gcd(nums):
    return reduce(_gcd, nums)
nums = [336, 360]
print("GCD of",','.join(str(e) for e in nums))
print(gcd(nums))
nums = [12, 17]
print("GCD of",','.join(str(e) for e in nums))
print(gcd(nums))
nums = [4, 6]
print("GCD of",','.join(str(e) for e in nums))
print(gcd(nums))
nums = [24, 30, 36]
print("GCD of",','.join(str(e) for e in nums))
print(gcd(nums))
