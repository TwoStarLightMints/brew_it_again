from django import forms

class RecipeForm(forms.Form):
    title = forms.CharField(max_length=100, label="Title", min_length=1, required=True)
    grinder_setting = forms.CharField(max_length=100, label="Grinder Setting", min_length=1, required=True)
    ratio = forms.CharField(max_length=100, label="Ratio", min_length=1, required=True)
    grams_coffee = forms.CharField(max_length=100, label="Grams of Coffee in", min_length=1, required=True)
    mili_water = forms.CharField(max_length=100, label="Mililiters of Water in", min_length=1, required=True)
    brew_time = forms.CharField(max_length=100, label="Brew Time", min_length=1, required=True)
