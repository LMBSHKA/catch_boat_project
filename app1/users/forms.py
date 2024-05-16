from pyexpat.errors import messages
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from users.models import User


    
class UserLoginForm(AuthenticationForm):
    username = forms.CharField()                              
    password = forms.CharField()
    class Meta():
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            #"first_name",
            #"last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
    
    #first_name = forms.CharField()
    #last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            #"last_name",
            "username",)
            #"email",)

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    #last_name = forms.CharField()
    username = forms.CharField()
    #email = forms.CharField()

class EditProfileForm(forms.ModelForm):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=("email", "username", "first_name", "last_name", "about")

