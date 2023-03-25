import logo
from classes.classes import Dices

print(logo.logo)

run_game = Dices()

stop_game = True
while stop_game:
    choose_dices = int(input('How many dices do you want to roll? '))
    run_game.roll_dices(choose_dices)
    replay = input('Do you want to roll dices again (Y/N)').casefold()
    if replay == 'n':
        stop_game = False

print(logo.game_end)
