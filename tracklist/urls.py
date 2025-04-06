from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tulip", views.tulip, name="tulip"),
    path("rose", views.rose, name="rose"),
]