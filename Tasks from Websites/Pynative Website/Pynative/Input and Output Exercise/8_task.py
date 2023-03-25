# Exercise 8: Format variables using a string.format() method.
# Write a program to use string.format() method to format the
# following three variables as per the expected output

totalMoney = 1000
quantity = 3
price = 450

print("I have {0} dollars so I can buy {1} football for {2}".
      format(totalMoney, quantity, float('%.3f' % price)))