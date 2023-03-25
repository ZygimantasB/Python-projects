class BankAccount:
    def __init__(self, account_type: int, name: str, balance: int):
        self.account_type = account_type
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawal(self, take_out_money):
        if self.balance < take_out_money:
            print('Not enough money in your bank account')
        else:
            self.balance = self.balance - take_out_money

    def bank_fees(self):
        self.balance = (95/100) * self.balance

    def display(self):
        print(f'{self.account_type},'
              f' {self.name}, '
              f'{self.balance}')
