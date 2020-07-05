from django.urls import path

from hello import views

urlpatterns = [
    path("", views.index0, name="index"),
    # path("<str:name>", views.greet1, name="greet"),
    # path("brian", views.brian, name="brian"),
    # path("david", views.david, name="david"),
]
