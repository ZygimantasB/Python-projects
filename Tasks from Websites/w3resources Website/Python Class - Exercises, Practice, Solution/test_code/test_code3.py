class Bike:
    name = "asdf"

    def __init__(self):  # Constructor
        self.name = 'James'

    def create_method(self):
        return f'{self.name}'


# bike1 = Bike('Mountain Bike')
bike1 = Bike()
# print(bike1)


print(bike1.create_method())
