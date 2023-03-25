# 59. Write a Python program to convert height (in feet and inches) to centimeters

people_height_feet = int(input("Please enter the people height in feet: "))
people_height_inches = int(input("Please enter the people height in inches: "))

height_cm = (people_height_feet * 30.48) + (people_height_inches * 2.54)

print(f"Converted height is {height_cm} cm")
print(f"Converted height is {round(height_cm)} cm")


print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)
