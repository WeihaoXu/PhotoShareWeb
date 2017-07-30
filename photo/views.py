from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm 
# Create your views here.

def index(request):
	return render(request, 'photo/index.html', {})

def signup(request):
	if request.method == 'POST':
		form = SingUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('index')
	else:
		form = SignUpForm()
	return render(request, 'photo/signup.html', {'form': form})

