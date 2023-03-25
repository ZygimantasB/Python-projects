from classes.exercise_43 import BankAccount

my_account = BankAccount(123456789, name='James', balance=27000)
my_account.withdrawal(500)
my_account.deposit(700)
my_account.deposit(400)
my_account.withdrawal(48000)
my_account.display()
