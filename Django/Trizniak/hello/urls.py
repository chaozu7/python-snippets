from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blizniak", views.blizniak, name="blizniak"),
    path("<str:name>", views.greet, name="greet"),
]
