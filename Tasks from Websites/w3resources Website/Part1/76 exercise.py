# 76. Write a Python program to get the command-line
# arguments (name of the script, the number of arguments, arguments) passed to a script.

import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))
