from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class SignUpForm(UserCreationForm):
	birth_date = forms.DateField(help_text='Format: YYY-MM-DD')
	class Meta:
		model = User
		fields = ('username', 'birth_date', 'password1', 'password2', 'email')

# As for login form: meant to create user login form by myself. However, there is existing AuthenticationFrom and I can just use that for login. 
# See doc at: https://docs.djangoproject.com/en/1.8/modules/django/contrib/auth/forms/

class LoginForm(forms.Form):
	username = forms.CharField(max_length=254)
	password = forms.CharField(max_length=254)


class UploadImgForm(forms.ModelForm):
	class Meta:
		model = models.Photo
		fields = ('name', 'data')






