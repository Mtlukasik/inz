from django.db import models
from django.template.defaultfilters import slugify
class Menu_Item(models.Model):
	name = models.CharField(max_length=32,unique=True)
	url = models.URLField()
	def __str__(self):
		return self.name
class Nazwa(models.Model):
	name = models.CharField(max_length=32,unique=True)
	slug = models.SlugField()
	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super(Nazwa,self).save(*args,**kwargs)	
	def __str__(self):
		return self.name
# Create your models here.
