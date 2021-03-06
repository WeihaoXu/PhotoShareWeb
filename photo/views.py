from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm, UploadImgForm, CreateStreamForm
from django.views.generic import TemplateView
from django.views import View # most basic view
from django.http import HttpResponse
from django.utils import timezone
from .models import Photo, Stream
from .helper_funcs import validate_user




def index(request):
	return render(request, 'photo/index.html')

class Home(View):
	def get(self, request):
		if(not validate_user(request)):
			return redirect('login')
		user = request.user	
		user_streams = Stream.objects.filter(owner=user) # shouldn't use get here. Get is to get an individual object.
		context = {
			'user': user,
			'user_streams': user_streams,
			
		} 
		return render(request, 'photo/home.html', context)

class Signup(View):
	def post(self, request):
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save() # user saved. post_save signal sent. Profile created.
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			context = {
				'user': request.user 
			}
			return redirect('home')
		return redirect('signup')
	def get(self, request):
		form = SignUpForm()
		context = {
			'form': form,
			'user': request.user	
		}
		return render(request, 'photo/signup.html', context)


	
class Login(View):
	def get(self, request):
		if(validate_user(request)):
			return redirect('home')
		form = AuthenticationForm() 
		context = {
			'user': request.user, 
			'form': form
		}
		return render(request, 'photo/login.html', context)

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if(user is not None):
			if(user.is_active):
				login(request, user)  # login() saves the user's ID in the session, using Django's session framework.
				return redirect('home') 
			else:
				return HttpResponse('disabled account!')
		else:
			return HttpResponse('username or password invalid!')


class Logout(View):
	def get(self, request):
		logout(request);
		return redirect('index')

class CreateStream(View):
	def get(self, request):
		if(not validate_user(request)):
			return redirect('login')	

		create_stream_form = CreateStreamForm()
		context = {
			"user": request.user,
			"form": create_stream_form,	
		}
		print(create_stream_form.as_p())
		return render(request, 'photo/create_stream.html', context)


	def post(self, request):
		if(not validate_user(request)):
			return HttpResponse("user authentication faild");
		form = CreateStreamForm(request.POST, request.FILES)
		if(form.is_valid()):
			name = form.cleaned_data['name']
			cover = form.cleaned_data['cover']
			description = form.cleaned_data['description']
			is_public = form.cleaned_data['public']
			stream = Stream(name=name, cover_img=cover, owner=request.user, description=description, is_public=is_public)
			stream.save()
			return redirect('home')
		else:
			return HttpResponse("create stream form invalid!")

# Display the photos in a photo stream. Upload button for the owner.
class Gallery(View):
	def get(self, request, stream_id):
		stream = Stream.objects.get(pk=stream_id)
		stream_photos = Photo.objects.filter(stream_belong=stream) 
		indexes = range(len(stream_photos))
		upload_img_form = UploadImgForm()
		is_owner = (request.user.pk == stream.owner.pk)
		context = {
			'user': request.user,
			'stream': stream,
			'form': upload_img_form,
			'photos': stream_photos,
			'indexes': indexes,
			'is_owner': is_owner,
		}
		return render(request, 'photo/gallery.html', context=context)
		#return HttpResponse("get stream id {0}".format(stream_id))

	def post(self, request, stream_id):
		if(not validate_user(request)):
			return redirect('login')
		stream = Stream.objects.get(pk=stream_id)
		for myfile in request.FILES.getlist('files'):
			photo = Photo()
			photo.stream_belong = stream
			photo.data.save(myfile.name, myfile)
			photo.save()
		return redirect('gallery', stream_id=stream.id)


class Global(View):
	def get(self, request):	
		shared_streams = Stream.objects.filter(is_public=True)
		context={
			'user': request.user,
			'shared_streams': shared_streams,
		}
		return render(request, 'photo/global.html', context)	

class Subscribed(View):
	def get(self, request):
		if(not validate_user(request)):
			return redirect('login')
		user = request.user	
		subscribed_streams = Stream.objects.filter(subscribers=user)
		context = {
			'user': user,
			'subscribed_streams': subscribed_streams,
			
		} 
		return render(request, 'photo/subscribed.html', context)

		
	
class DeletePhoto(View):
	def get(self, request, photo_id, stream_id):
		# in order to redirect to the gallery page, cache might be used. Research it later.
		Photo.objects.get(pk=photo_id).delete()
		return redirect('gallery', stream_id=stream_id)
		#return HttpResponse("delete request of {} received".format(photo_id))

class DeleteStream(View):
	def get(self, request, stream_id):
		Stream.objects.get(pk=stream_id).delete()
		return redirect('home')

class SubscribeStream(View):
	def get(self, request, stream_id):
		if(not validate_user(request)):
			return redirect('login')
		s = Stream.objects.get(pk=stream_id)
		subscribers = s.subscribers.filter(pk=request.user.pk)
		if(len(subscribers) == 0):
			s.subscribers.add(request.user)
		else:
			# alert "already subscribed"
			None
		return redirect('global')

class UnsubscribeStream(View):
	def get(self, request, stream_id):
		if(not validate_user(request)):
			return redirect('login')
		s = Stream.objects.get(pk=stream_id)
		s.subscribers.remove(request.user)
		return redirect('home')












