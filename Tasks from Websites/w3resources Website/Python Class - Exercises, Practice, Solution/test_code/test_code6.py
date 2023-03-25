class Animals:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

    def __str__(self):
        return f'{self.color}, {self.legs}'


animals_list = []

animals1 = Animals('Black', 5)
animals2 = Animals('Red', 6)
animals3 = Animals('Green', 7)
animals4 = Animals('Blue', 8)

animals_list.append(animals1)
animals_list.append(animals2)
animals_list.append(animals3)
animals_list.append(animals4)

# for i in animals_list:
#     print(i.color, i.legs)

new_value = [(i.color, i.legs) for i in animals_list]
print(new_value)


