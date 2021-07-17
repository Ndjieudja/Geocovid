from django import forms
from .models import ProfileUser
from django.contrib.auth.forms import UserCreationForm

# put your forms there


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class CreateForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 'type':'password', 'align':'center', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 'type':'password', 'align':'center', 'placeholder':'Confirm Passwords'}),
    )

    class Meta:
        model = ProfileUser
        exclude = ('create', 'manage', 'user')