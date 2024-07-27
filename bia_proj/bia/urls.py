from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('recipe/<int:recipe_id>', views.view_recipe, name="recipe"),
    path('delete_recipe/<int:recipe_id>', views.delete_recipe, name="delete_recipe"),
    path('new_recipe', views.create_recipe, name="new_recipe"),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
