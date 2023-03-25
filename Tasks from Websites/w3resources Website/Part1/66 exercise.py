# 66. Write a Python program to calculate body mass index.

height = float(input("Please enter you Height in cm: "))
weight = float(input("Please enter your weight in kg: "))

bmi = (weight / height / height) * 10000

print(f"you BMI is {round(bmi,2)}")