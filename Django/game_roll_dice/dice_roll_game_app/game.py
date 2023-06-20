from random import randint


class DiceRollerGame:
    def __init__(self, num_dice: int = 1, num_sides: int = 6):
        self.num_dice = num_dice
        self.num_sides = num_sides
        self.history = []

    @property
    def num_dice(self) -> int:
        return self._num_dice

    @num_dice.setter
    def num_dice(self, value) -> None:
        if not 1 <= value <= 5:
            raise ValueError("Number of sides should be between 1 and 5")
        self._num_dice = value

    @property
    def num_sides(self) -> int:
        return self._num_sides

    @num_sides.setter
    def num_sides(self, value) -> None:
        if not 1 <= value <= 100:
            raise ValueError("Number of sides should be between 1 and 100")
        self._num_sides = value

    def roll(self) -> list:
        result = [randint(1, self.num_sides) for _ in range(self.num_dice)]
        self._add_to_history(result)
        return result

    def _add_to_history(self, result) -> None:
        self.history.append(result)
        if len(self.history) > 10:
            self.history.pop(0)


# num_dice = int(input("Enter the number of dice: "))
# num_sides = int(input("Enter the number of sides per dice: "))
#
# dice_roller = DiceRollerGame(num_dice=num_dice, num_sides=num_sides)
#
# result = dice_roller.roll()
# print(result)
#
# result = dice_roller.roll()
# print(result)
#
# print(dice_roller.history)
