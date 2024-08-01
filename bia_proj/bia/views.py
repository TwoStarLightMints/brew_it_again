from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RecipeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CoffeeRecipeEntry

def home(request):
    return render(request, "home.html")

def dashboard(request):
    users_prev_recipes = CoffeeRecipeEntry.objects.all().filter(owner=request.user)
    return render(request, "dashboard.html", { "user_recipes": users_prev_recipes })

def view_recipe(request, recipe_id):
    if request.user.is_authenticated:
        if CoffeeRecipeEntry.objects.filter(owner=request.user, id=recipe_id).count() > 0:
            recipe = CoffeeRecipeEntry.objects.get(owner=request.user, id=recipe_id)

            return render(request, "recipe_view.html", { "recipe": recipe })
        else:
            return render(request, "recipe_not_found.html")
    else:
        return redirect("login")

def create_recipe(request):
    if request.method == "GET":
        return render(request, "new_recipe.html",
                      {
                          "form": RecipeForm(),
                          "ratio": request.session.pop("ratio", ""),
                          "w_or_c": request.session.pop("w_or_c", "") == "water",
                          "input_amount": request.session.pop("input_amount", ""),
                          "result_amount": request.session.pop("result_amount", ""),
                      })
    elif request.method == "POST":
        form = RecipeForm(request.POST)

        if form.is_valid():
            new_recipe = CoffeeRecipeEntry()

            new_recipe.owner = request.user
            new_recipe.title = form.cleaned_data["title"]
            new_recipe.grinder_setting = form.cleaned_data["grinder_setting"]
            new_recipe.ratio = form.cleaned_data["ratio"]
            new_recipe.grams_coffee = form.cleaned_data["grams_coffee"]
            new_recipe.mili_water = form.cleaned_data["mili_water"]
            new_recipe.brew_time = form.cleaned_data["brew_time"]

            new_recipe.save()

            return redirect("dashboard")

def delete_recipe(request, recipe_id):
    if CoffeeRecipeEntry.objects.filter(owner=request.user, id=recipe_id).count() > 0 and request.user.is_authenticated:
        CoffeeRecipeEntry.objects.get(owner=request.user.is_authenticated, id=recipe_id).delete()
        
        return redirect("dashboard")
