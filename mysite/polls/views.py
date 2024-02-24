from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cat, Dog, User
from django.views import generic, View
from django.utils.html import escape


# Create your views here.
def users(request):
    users = User.objects.values("id", "name")
    print(users)
    context = {"users": users}
    return render(request, "users.html", context)


def user_details(request, id):
    user = User.objects.filter(id=int(id)).all()
    context = {"user_detail": user}
    return render(request, "user.html", context)


class ListView(View):
    model = Cat

    def get(self, request):
        modelname = self.model._meta.verbose_name.title().lower()
        stuff = self.model.objects.all()
        context = {f"{modelname}_list": stuff}
        return render(request, f"animals/{modelname}_list.html", context)


class DetailView(View):
    model = Cat

    def get(self, request, id):
        modelname = self.model._meta.verbose_name.title().lower()
        name = self.model.objects.filter(id=int(id)).values("name")
        context = {f"{modelname}_detail": name}
        return render(request, f"animals/{modelname}_detail.html", context)


class CatsListView(ListView):
    model = Cat


class CatDetailView(DetailView):
    model = Cat


class DogsListView(ListView):
    model = Dog


class DogDetailView(DetailView):
    model = Dog


def rest(request, guess):
    return HttpResponse(f"The integer value passed in the URL is: {guess}")


class Danger(View):
    def get(self, request):
        html = (
            """<html><body><p>Your guess was """
            + request.GET["guess"]
            + """</p></body></html>"""
        )

        return render(request, html)


def danger(request):
    html = f"""<html><body><p>Your guess was {request.GET.get('guess')}</p></body></html>"""
    return HttpResponse(html)


class Redirect(View):
    def get(self, request):
        return HttpResponseRedirect("http://127.0.0.1:8000/polls")
