from django.conf.urls import patterns, url
from ele import views
urlpatterns = patterns('',
	url(r'^$', views.index, name= 'index'),
	url(r'^lol/', views.lol, name= 'lol'))
