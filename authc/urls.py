from django.urls import include, path
from . import views

app_name = "authc"
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("open/", views.OpenView.as_view(), name="open"),
    path("apereo/", views.ApereoView.as_view(), name="apereo"),
    path("manual_protect/", views.ManualProtect.as_view(), name="manual_protect"),
    path("protect_view/", views.ProtectView.as_view(), name="protect_view"),
    path("dump_python/", views.DumpPython.as_view(), name="dump_python"),
    path("example/", views.example, name="example"),
]
