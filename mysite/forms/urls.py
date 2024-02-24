from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "forms"
urlpatterns = [
    path("guess", views.GuessGame.as_view(), name="guess_form"),
    path("", TemplateView.as_view(template_name="authz/main.html")),
    path("", TemplateView.as_view(template_name="registration/login.html")),
]
