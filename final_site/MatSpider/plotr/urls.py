from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("response.html", views.response),

    path("plotr/", views.plotr, name="plotr"),


]