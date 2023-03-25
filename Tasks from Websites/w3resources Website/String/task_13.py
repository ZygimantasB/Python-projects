# 13. Write a Python script that takes input from the user and
# displays that input back in upper and lower cases.

def print_back_upper_lower_string(inpt_string):
    return inpt_string[::-1], inpt_string.upper(), inpt_string.lower()


print(print_back_upper_lower_string("ThE qUiCk BrOwn FoX jUmPeD "
                                    "OvEr ThE LaZy DoG."))

