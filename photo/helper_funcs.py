from django import template
import copy

def validate_user(request):
	if(request.user.is_authenticated()):
		return True
	return False

