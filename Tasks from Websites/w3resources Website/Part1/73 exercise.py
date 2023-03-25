# 73. Write a Python program to calculate midpoints of a line.

x_1 = int(input("Please enter x1: "))
x_2 = int(input("Please enter x2: "))
y_1 = int(input("Please enter y1: "))
y_2 = int(input("Please enter y2: "))

midpoint = (x_1 + x_2) / 2, (y_1 + y_2) / 2

print(f"The mid point of x: {midpoint[0]}, the mid point of y: {midpoint[1]}")

# Other solution

print('\nCalculate the midpoint of a line :')

x1 = float(input('The value of x (the first endpoint) '))
y1 = float(input('The value of y (the first endpoint) '))

x2 = float(input('The value of x (the first endpoint) '))
y2 = float(input('The value of y (the first endpoint) '))

x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2
print();
print("The midpoint of line is :")
print( "The midpoint's x value is: ",x_m_point)
print( "The midpoint's y value is: ",y_m_point)
print();
