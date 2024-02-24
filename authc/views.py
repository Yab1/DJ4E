from django.shortcuts import render, redirect
from django.views import View
from django.utils.http import urlencode
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BasicForm
from django.http import HttpResponse


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, "authc_template.html")


class OpenView(View):
    def get(self, request):
        return render(request, "open.html")


class ApereoView(View):
    def get(self, request):
        return render(request, "apereo.html")


class ManualProtect(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "manual.html")
        loginurl = reverse("login") + "?" + urlencode({"next": request.path})
        return redirect(loginurl)


class ProtectView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "protected.html")


class DumpPython(View):
    def get(self, request):
        return render(request, "dump.html")


def example(request):
    old_data = {"title": "Saki Car", "mileage": 42, "purchase_date": "2024-02-24"}
    form = BasicForm(old_data)
    context = {"form": form}
    return render(request, "example_form.html", context)
