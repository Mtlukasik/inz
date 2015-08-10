from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	context_dict = {'boldmessage': "i am bold font from the context"}
	return render(request,'ele/index.html',context_dict)
def lol(request):
	return HttpResponse('heheh')
# Create your views here.
