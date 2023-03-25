from classes.task_43_class import BankAccount

check_account = BankAccount(account_number=123456789, name='Wade Wilson', balance=8452)

check_account.withdrawal(500)
check_account.withdrawal(453)
check_account.deposit(57)
check_account.bank_fees()

print(check_account.display())
