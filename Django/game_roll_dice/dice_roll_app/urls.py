from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='dice_roll_app-home'),
    ]
