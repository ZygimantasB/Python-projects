# 150. Write a Python function to check whether a distinct
# pair of numbers whose product is odd present in a sequence of integer values.

def odd_product(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if  i != j:
                product = nums[i] * nums[j]
                if product & 1:
                    return True
    return False
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]
print(dt1, odd_product(dt1));
print(dt2, odd_product(dt2));
print(dt3, odd_product(dt3));
