from django.urls import path
from hello import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nok", views.nok, name='nok'),
    path("<str:name>", views.greet, name='greet'),
]
