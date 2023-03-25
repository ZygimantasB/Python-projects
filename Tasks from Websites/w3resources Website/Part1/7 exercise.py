# 7. Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

filename = input("Please enter the file name: ")
filename_extension = filename.split(".")
print(f"The filename extension are {filename_extension[-1]}")

# not my solution
# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print ("The extension of the file is : " + repr(f_extns[-1]))