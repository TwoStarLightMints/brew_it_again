from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('recipe/<int:recipe_id>', views.view_recipe, name="recipe"),
    path('new_recipe', views.create_recipe, name="new_recipe")
]

