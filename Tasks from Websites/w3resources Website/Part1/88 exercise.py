# 88. Given variables x=30 and y=20, write a Python program to print "30+20=50"

x = 30
y = 20

sum = x + y

print(f"{30} + {20} = {sum}")

print("{0} + {1} = {2}".format(x, y, sum))

print("%d + %d = %d" % (x, y, x+y))