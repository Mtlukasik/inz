from django.db import models
from django.template.defaultfilters import slugify
class Category(models.Model):
        name = models.CharField(max_length=128, unique=True)

        slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name
class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)	
	url = models.URLField()
	def __str__(self):
		return self.title

# Create your models here.
