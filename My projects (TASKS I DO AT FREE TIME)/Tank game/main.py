from classes.tank import Tank


tank = Tank()

for value in Tank.information_about_the_game():  # I do what because I want to use less print
    print(value)

tank.game_functionality()
