from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
	def __str__(self):
		string = """
			user:{0},
			bio:{1},
			location: {2},
			birth_date:{3}
		""".format(self.user, self.bio, self.location, self.birth_date)
		return string


	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()


class Stream(models.Model):
	cover_img = models.ImageField(upload_to='cover_imgs/', blank=True) 
	name = models.CharField(max_length=30, blank=False) #blank is default false
	description = models.TextField(max_length=500, blank=True)
	create_date = models.DateField(auto_now_add=True) 
	# if null==true, django will store empty values as NULL in the database. Default False
	update_date = models.DateField(null=False, blank=False)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_owner')
	subscribers = models.ManyToManyField(User, related_name='stream_subscribers' )

class Photo(models.Model):
	def Photo(self, data):
		self.data = data
	name = models.CharField(max_length=30, blank=True) #name optional
	description = models.TextField(max_length=500, blank=True)
	create_date = models.DateField(auto_now_add=True)
	update_date = models.DateField(auto_now=True)
	stream_belong = models.ForeignKey(Stream, on_delete=models.CASCADE, blank=True, null=True)
	data = models.ImageField(upload_to = 'imgs/', blank=False)

class Comments(models.Model):
	text = models.TextField(max_length=500, blank=False)
	date = models.DateField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE) 
	photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

	



	
	


	

	


