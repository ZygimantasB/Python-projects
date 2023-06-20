from django.shortcuts import render
from django.views import View

from .game import DiceGame


class HomeView(View):
    template_name = 'dice_roll_app/home.html'

    def get(self, request):
        request.session['game'] = {'user_input': 0, 'dice_sides': [], 'history': []}
        return render(request, self.template_name)

    def post(self, request):
        game_data = request.session.get('game', {'user_input': 0, 'dice_sides': [], 'history': []})
        game = DiceGame(game_data['user_input'], game_data['dice_sides'], game_data['history'])
        error_message = None

        user_input = request.POST.get('user_input')

        if user_input and 1 <= int(user_input) <= 5:
            game.user_input = int(user_input)
            dice_sides = [int(request.POST.get(f'dice_sides_{i}')) for i in range(1, game.user_input + 1) if request.POST.get(f'dice_sides_{i}') != '']
            for side in dice_sides:
                if not (1 <= side <= 100):
                    error_message = "Please enter a number between 1 and 100 for each dice side"
                    break
            else:
                game.dice_sides = dice_sides
        else:
            error_message = "Please enter a number between 1 and 5 for the number of dice"

        if error_message is None:
            game.roll_dice()
            game_data = {'user_input': game.user_input,
                         'dice_sides': game.dice_sides,
                         'history': game.history}
            request.session['game'] = game_data

        return render(request, self.template_name, {'user_input': game.user_input,
                                                    'dice_sides': game.dice_sides,
                                                    'history': game.history,
                                                    'error_message': error_message})
