from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
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
""""
class UserUpdateForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def clean_email(self):

        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email адрес должен быть уникальным')
        return email


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('slug', 'birth_date', 'bio', 'avatar')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })
"""