from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

# Create your views here.

def login_page(request):
    if request.method == "GET":
        return render(request, "login.html", { 'login_form': LoginForm() })
    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])

            if user is not None:
                login(request, user)

                return redirect("/dashboard")
            else:
                return render(request, "wrong.html")
        else:
            return render(request, "wrong.html")

def logout_page(request):
    logout(request)
    return redirect("home")
