from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, required=True)
    password = forms.CharField(label="Password", max_length=100, required=True, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, required=True)
    password = forms.CharField(label="Password", max_length=100, required=True, widget=forms.PasswordInput)
