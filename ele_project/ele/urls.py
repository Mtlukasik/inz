from django.conf.urls import patterns, url
from ele import views
urlpatterns = patterns('',
	url(r'^$', views.index, name= 'index'),
	url(r'^lol/', views.lol, name= 'lol'),
	url(r'^nazwa/(?P<nazwa_name_slug>[\w-]+)/$',views.nazwa, name='nazwa'),)
