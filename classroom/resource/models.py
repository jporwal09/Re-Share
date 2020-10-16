from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Topic(models.Model):
	name = models.CharField(max_length=500,null=False,blank=False)
	created = models.DateTimeField('date created', default = timezone.now)
	last_updated = models.DateTimeField('last updated', default = timezone.now)
	user =  models.ForeignKey(User,on_delete=models.PROTECT)

	def __str__(self):
		return self.name


class Material(models.Model):
	url = models.URLField(null = False)
	topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
	desc =  models.TextField(max_length=500,default = 'None')
	created = models.DateTimeField('date created',default = timezone.now)
	last_updated = models.DateTimeField('last updated',default = timezone.now)
	user = models.ForeignKey(User,on_delete = models.PROTECT)
	likes = models.ManyToManyField(User, related_name = 'Material_op')
	fav = models.ManyToManyField(User,related_name='favorite')

	@property
	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.url




