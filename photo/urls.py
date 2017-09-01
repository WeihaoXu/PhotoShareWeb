from django.conf.urls import url
from . import views
import django.contrib.auth.views as auth_views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/', views.Home.as_view(), name='home'),
	url(r'^signup/', views.Signup.as_view(), name='signup'),
	url(r'^login/',  views.Login.as_view(), name='login'),
	url(r'^logout/', views.Logout.as_view(), name='logout'),
	url(r'^create_stream/', views.CreateStream.as_view(), name='create_stream'),
	url(r'^gallery/(?P<stream_id>[0-9]+)$', views.Gallery.as_view(), name='gallery'), 
	url(r'^moments/', views.Moments.as_view(), name='moments'),
]
