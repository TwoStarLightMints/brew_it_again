from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Stored Coffee Recipe
class CoffeeRecipeEntry (models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    grinder_setting = models.IntegerField()
    ratio = models.CharField(max_length=6)
    grams_coffee = models.IntegerField()
    mili_water = models.IntegerField()
    brew_time = models.CharField(max_length=6)
