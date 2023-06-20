class DiceGame:
    def __init__(self, user_input=0, dice_sides=None, history=None):
        self.user_input = user_input
        self.dice_sides = dice_sides
        self.history = history

    def roll_dice(self):
        roll_result = [side for side in self.dice_sides]
        self.history.append(roll_result)
        if len(self.history) > 10:
            self.history.pop(0)
