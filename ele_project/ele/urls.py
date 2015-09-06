from django.conf.urls import patterns, url
from ele import views
urlpatterns = patterns('',
	url(r'^$', views.index, name= 'index'),
	url(r'^ostronie/', views.ostronie),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category),
	url(r'^image/(?P<n>[\w\-]+)/$', views.graph),
	url(r'^page/(?P<n>[\w\-]+)/$', views.graphic),)
