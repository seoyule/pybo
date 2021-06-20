from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm): #폼
    email = forms.EmailField(label = '이메일')

    class Meta():
        model = User     #모델
        fields = ['username','email']


