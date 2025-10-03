from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserInfo

# Form for UserInfo (profile details)
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ["age", "city", "hobby", "favorite_food"]

# Form for Sign Up
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
