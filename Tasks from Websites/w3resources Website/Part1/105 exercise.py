# 105. Write a Python program to get the users environment.

import os
import pprint

print(os.environ)


# User's environment variables
u_env_var = os.environ
print("User's Environment variable:")
pprint.pprint(dict(u_env_var), width = 1)