# from django.test import TestCase
# from .views import DiceGame
#
#
# # Create your tests here.
#
# class DiceGameTest(TestCase):
#     def setUp(self):
#         # self.game = DiceGame()
#         self.game = DiceGame(user_input=4, user_input_dice_sides=10, history=[])

    # def test_roll_dice(self):
    #     self.game.user_input = 2
    #     self.game.user_input_dice_sides = 6
    #     self.game.roll_dice()
    #     self.assertEqual(len(self.game.history), 1)
    #     self.assertEqual(len(self.game.history[0]), 2)
    #     self.assertTrue(all([1 <= roll <= 6 for roll in self.game.history[0]]))

    # def test_roll_dice_history(self):
    #     self.game.user_input = 2
    #     self.game.user_input_dice_sides = 6
    #     self.game.roll_dice()

    # def test_dice_roll_history(self):
    #     for _ in range(11):
    #         self.game.roll_dice()
    #     self.assertEqual(len(self.game.history), 11)
