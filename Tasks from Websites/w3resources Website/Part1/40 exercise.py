# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math


p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)

a1 = [10, 6]
a2 = [7, 9]

distance1 = math.sqrt(a1[0]-a2[0])

print(distance1)