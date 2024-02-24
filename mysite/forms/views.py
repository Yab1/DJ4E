from urllib import response
from django.shortcuts import redirect, render
from django.views import View
from django.utils.html import escape
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def main(request):
    num_visitors = request.session.get("num_visitors", 0) + 1
    request.session["num_visitors"] = num_visitors
    if num_visitors >= 4:
        del request.session["num_visitors"]
    return HttpResponse(f"Number of Visitors {num_visitors}")


def checkGuess(guess):
    msg = False
    if guess:
        try:
            if int(guess) < 42:
                msg = "Your Guess is too low"
            elif int(guess) > 42:
                msg = "Your Guess is too high"
            else:
                msg = "Congratulations!"
        except:
            msg = f"Bad format for guess {escape(guess)}"
    return msg


class GuessGame(View):
    def get(self, request):
        msg = request.session.get("msg", False)
        if msg:
            del request.session["msg"]
        context = {"message": msg}
        return render(request, "guess_form.html", context)

    def post(self, request):
        guess = request.POST.get("guess")
        msg = checkGuess(guess)
        request.session["msg"] = msg
        return redirect(request.path)


class DumpPython(View):
    def get(self, request):
        response = "<pre/>\nUser Data in Python:\n\n"
        response += f"Login url: {reverse('login')}\n"
        response += f"Login url: {reverse('logout')}\n\n"
        return HttpResponse(response)
