import random, data


class Dices:

    def roll_dices(self, how_many_dices):
        for _ in range(how_many_dices):
            random_number = random.randint(0, 5)
            print(data.dices[random_number], end=',')
