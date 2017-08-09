from django import template
import copy

def validate_user(request):
	if(request.user.is_authenticated()):
		return True
	return False

# used to make map work in templates
register = template.Library()
@register.simple_tag
def dictKeyLookup(the_dict, key):
   # Try to fetch from the dict, and if it's not found return an empty string.
      return the_dict.get(key, '')

def rename_form_attr(form):
	if not (hasattr(form.Meta, 'field_map') and hasattr(form.Meta, 'fields')):
		return False
	for key in form.fields.keys():
		form.fields[key].label_tag = form.Meta.field_map[key] 
		#form.fields[key] = None
	#for field in form:
	#	print(field.label_tag)
		#field.label_tag = form.Meta.field_map[field.label_tag]
	return True

	
