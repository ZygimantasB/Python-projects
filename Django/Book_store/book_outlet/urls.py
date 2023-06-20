from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>", views.book_detail, name="book-detail")
    ]
