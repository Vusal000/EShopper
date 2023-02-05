from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label=("Confirm password"))

    class Meta:
        model = User
        fields = ("fisrt_name",'last_name', 'username', 'email', 'image', 'password','password2')

        