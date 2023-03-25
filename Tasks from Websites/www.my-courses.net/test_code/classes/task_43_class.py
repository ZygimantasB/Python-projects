class BankAccount:
    def __init__(self, account_number: int, name: str, balance: int):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, add_money):
        self.balance = self.balance + add_money

    def withdrawal(self, take_out_money):
        if self.balance < take_out_money:
            print('Out of money')
        else:
            self.balance = self.balance - take_out_money

    def bank_fees(self):
        self.balance = (95/100) * self.balance

    def display(self):
        print(f'Your account number: {self.account_number}\n'
              f'Your name: {self.name}\n'
              f'Your balance: {self.balance}\n')
