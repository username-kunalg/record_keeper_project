from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

class RecordForm(forms.ModelForm):
    """Form for creating and updating Record objects."""

    class Meta:
        model = Record
        fields = '__all__'
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 4})  # Customize textarea appearance
        }


class SignupForm(UserCreationForm):
    """Form for user signup."""

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    """Form for user login."""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)