from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm

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

def register_page(request):
    if request.method == "GET":
        return render(request, "register.html", { "form": RegisterForm() })
    elif request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(username=form.cleaned_data["username"], password=form.cleaned_data["password"])

            new_user.save()

            return redirect("login")

def logout_page(request):
    logout(request)
    return redirect("home")
