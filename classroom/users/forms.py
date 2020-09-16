from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    First_Name = forms.CharField()
    Last_Name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','First_Name','Last_Name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already used by some other user.")
        return email    
