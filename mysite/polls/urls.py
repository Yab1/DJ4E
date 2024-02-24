from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.users, name="users"),
    path("user/<int:id>", views.user_details, name="user_details"),
    path("template", TemplateView.as_view(template_name="main.html"), name="template"),
    path("rest/<int:guess>", views.rest, name="rest"),
    path("danger", views.danger, name="danger"),
    path("redirect", views.Redirect.as_view(), name="redirect"),
    path("cats", views.CatsListView.as_view(), name="cats"),
    path("cat/<int:id>", views.CatDetailView.as_view(), name="cat_detail"),
    path("dogs", views.DogsListView.as_view(), name="dogs"),
    path("dogs/<int:id>", views.DogDetailView.as_view(), name="dog_detail"),
]
