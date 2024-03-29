
from users.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={''
                            'class':'appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm',
                            'type':'text',
                            'placeholder':'Enter your username',
                            'id': 'username' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'type' : "password",
        'id' : "password",
        'autocomplete':'current-password',
    'class' : "appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" ,
    'placeholder': 'Enter your password'
    }))
    class Meta:
        model = User
        fields = ('username', 'password')