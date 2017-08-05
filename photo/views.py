from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm
from django.views.generic import TemplateView
from django.views import View # most basic view
from django.http import HttpResponse




def index(request):
	context = {'login_out': 'login'}
	return render(request, 'photo/index.html', context)

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save() # user saved. post_save signal sent. Profile created.
			user.refresh_from_db() #reloads user from db. Profile loaded.
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return render(request, 'photo/index.html', {'login_out': user.username})
	else:
		form = SignUpForm()
		context = {
			'form': form,
			'login_out': "sf",	
			}
		return render(request, 'photo/signup.html', context)

	
class Login(View):
	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if(user is not None):
			if(user.is_active):
				login(request, user)  # login() saves the user's ID in the session, using Django's session framework.
				return render(request, 'photo/index.html', {'login_out': username})
			else:
				return HttpResponse('disabled account!')
		else:
			return HttpResponse('username or password invalid!')


	def get(self, request):
		form = AuthenticationForm() 
		context = {
			'login_out': '',
			'form': form
		}
		return render(request, 'photo/login.html', context)
		
	











