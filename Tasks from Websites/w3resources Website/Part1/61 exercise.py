# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.

distance = int(input("Please enter distance in feet. "
                     "Everything will be converted to inches yards "
                     "and miles: "))

distance_inches = distance * 12
distance_yards = distance * (1/3)
distance_miles = distance * 0.000189394

print(f"Inches: {distance_inches}")
print(f"Yards: {distance_yards}")
print(f"Miles: {distance_miles}")

distance1 = int(input("Please enter the distance in yard: "))

distance1_feet = distance1 * 3
distance1_inches = distance1 * 36

print(f"Feet: {distance1_feet}")
print(f"Inches: {distance1_inches}")

distance2 = int(input("Please enter the distance in miles: "))

distance2_yards = distance2 * 1768
distance2_feet = distance2 * 5280

print(f"Yards {distance2_yards}")
print(f"Feet {distance2_feet}")

d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3.0
d_miles = d_ft / 5280.0

print("The distance in inches is %i inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)