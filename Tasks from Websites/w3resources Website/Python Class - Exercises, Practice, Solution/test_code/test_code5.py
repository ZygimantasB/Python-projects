class Cat1:
    color = 'silver'

    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

    def __str__(self):
        return f'{self.color} {self.legs}'

    def miaukseti(self):
        return print('Miau')

    def wolf(self):
        return print('Auuuuu')

    def __move_legs(self):
        pass

    def look_there_run(self):
        pass

    def run(self):
        self.__move_legs()
        self.look_there_run()
        return 'Running'


cat1 = Cat1('black', 4)
print(cat1)
print(cat1.color)
print(cat1.legs)
cat1.miaukseti()
cat1.wolf()
print(cat1.run(), cat1.legs, cat1.color)
