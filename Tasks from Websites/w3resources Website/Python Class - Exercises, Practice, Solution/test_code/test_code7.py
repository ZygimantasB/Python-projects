class Cat:
    def __init__(self, name, age, color='black'):
        self.name = name
        self.age = age
        self.color = color

    def cat_sound(self, cat_sound='miau', times=1):
        print(cat_sound * times)

    def __str__(self):
        return f'Cat name {self.name}'

    # def __repr__(self):
    #     return f'Cat name {self.name}'


cats = []

while True:
    pasirinkimas = int(input('Pasirinkimas:\n1 - ivesti kate \n2 - perzziureti visas kates'
                             '\n3 - iseiti is programos\n'))
    if pasirinkimas == 1:
        name = input('Ivesti kates varda: ')
        age = int(input('Ivesti kates amziu: '))
        color = input('Ivesti kates spalva: ')
        cat = Cat(name, age, color)
        cats.append(cat)
    if pasirinkimas == 2:
        for cat in cats:
            print(cat)
    if pasirinkimas == 3:
        print('Viso gero')
        break