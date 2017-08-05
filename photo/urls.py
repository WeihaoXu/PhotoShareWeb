from django.conf.urls import url
from . import views
import django.contrib.auth.views as auth_views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signup/', views.signup, name='signup'),
	url(r'^login/',  views.Login.as_view(), name='login'),
	#url(r'^logout/', views.Logout.as_view(), name='logout'),
]
