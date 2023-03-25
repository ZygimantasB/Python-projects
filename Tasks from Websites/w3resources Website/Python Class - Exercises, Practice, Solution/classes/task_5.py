class DefineFunction:
    def __init__(self, name, surname, curse, sex):
        self.name = name
        self.surname = surname
        self.curse = curse
        self.sex = sex

    def __str__(self):
        return f'{self.name},{self.surname},{self.curse},{self.sex}'
