from django.shortcuts import render
from django.views import View

from .game import DiceRollerGame


# Create your views here.


class StartGameView(View):
    template_name = "dice_roll_game_app/start_game.html"
    dice_game = DiceRollerGame()

    def get(self, request):
        return render(request, template_name=self.template_name)

    def post(self, request):
        self.dice_game.user_input = int(request.POST.get("user_input", 1))
        self.dice_game.num_dice = int(request.POST.get("num_dice"))
        self.dice_game.dice_sides = [int(request.POST.get(f"dice_sides_{i}")) for i in range(1, self.dice_game.user_input + 1) if request.POST.get(f"dice_sides_{i}") != ""]
        return render(request, template_name=self.template_name, context={"user_input": self.dice_game.user_input,
                                                                        "num_dice": self.dice_game.dice_sides,
                                                                        "history": self.dice_game.history})
