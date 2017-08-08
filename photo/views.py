from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm, UploadImgForm
from django.views.generic import TemplateView
from django.views import View # most basic view
from django.http import HttpResponse
from .models import Photo




def index(request):
	context = {'user': request.user} 
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
			context = {
				'user': request.user 
			}
			return render(request, 'photo/index.html', context)
	else:
		form = SignUpForm()
		context = {
			'form': form,
			'user': request.user	
		}
		return render(request, 'photo/signup.html', context)
		#return HttpResponse("sign up request get")

	
class Login(View):
	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if(user is not None):
			if(user.is_active):
				login(request, user)  # login() saves the user's ID in the session, using Django's session framework.
				return render(request, 'photo/index.html', {'user': request.user})
			else:
				return HttpResponse('disabled account!')
		else:
			return HttpResponse('username or password invalid!')


	def get(self, request):
		form = AuthenticationForm() 
		context = {
			'user': request.user, 
			'form': form
		}
		return render(request, 'photo/login.html', context)

class Logout(View):
	def get(self, request):
		logout(request);
		return redirect('index')

class UploadImg(View):
	def get(self, request):
		form = UploadImgForm();
		context = {
			'user': request.user,
			'form': form
		}
		return render(request, 'photo/upload_img.html', context);
	def post(self, request):
		form = UploadImgForm(request.POST, request.FILES)
		if(form.is_valid()):
			photo = Photo(data = request.FILES['data'])
			photo.name = request.POST['name']
			photo.save()
		return redirect('index')

		

		

	
		
	











