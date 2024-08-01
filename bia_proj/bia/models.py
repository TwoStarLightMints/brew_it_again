from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Stored Coffee Recipe
class CoffeeRecipeEntry (models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    grinder_setting = models.IntegerField()
    ratio = models.CharField(max_length=6)
    grams_coffee = models.FloatField(max_length=12)
    mili_water = models.FloatField(max_length=12)
    brew_time = models.CharField(max_length=6)
