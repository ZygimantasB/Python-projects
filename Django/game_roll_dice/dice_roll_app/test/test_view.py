from django.test import TestCase, Client
from django.urls import reverse
from dice_roll_app.views import HomeView, DiceGame


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('dice_roll_app-home')
        self.game = DiceGame()

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dice_roll_app/home.html')

        self.assertNotContains(response, '<div class="alert alert-danger" role="alert">')

    def test_home_POST(self):
        response = self.client.post(self.home_url, {
            'user_input': 1,
            'user_input_dice_sides': 6
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dice_roll_app/home.html')

        self.assertContains(response, '<h2>Result</h2>')

    def test_home_POST_invalid_user_input(self):
        response = self.client.post(self.home_url, {
            'user_input': 1,
            'user_input_dice_sides': 6
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dice_roll_app/home.html')

    def test_home_POST_invalid_user_input_dice_sides(self):
        response = self.client.post(self.home_url, {
            'user_input': 1,
            'user_input_dice_sides': 0
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dice_roll_app/home.html')

        self.assertContains(response, '<div class="alert alert-danger" role="alert">')

    def test_home_view(self):
        response = self.client.get(self.home_url)

        self.assertContains(response, '<title>🎲 Play The Game</title>')
