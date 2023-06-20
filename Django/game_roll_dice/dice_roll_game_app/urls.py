from django.urls import path
from .views import StartGameView

urlpatterns = [
        path("", StartGameView.as_view(), name="start_game"),
    ]
