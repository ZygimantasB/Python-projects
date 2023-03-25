# 13. Write a Python program to print the following 'here document'.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

print('-' * 50)

print("\n"
      "a string that you 'don't' have to escape\n"
      "This\n"
      "is a  ....... multi-line\n"
      "heredoc string --------> example")