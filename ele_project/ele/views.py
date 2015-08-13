from django.shortcuts import render
from django.http import HttpResponse
from ele.models import Menu_Item
from ele.models import Nazwa
def index(request):#odpowiedzialny za widok glownej strony
	menu1 = Nazwa.objects.order_by('-name')[:5]
	context_dict = {'nazwy': menu1}
	return render(request,'ele/index.html',context_dict)
def lol(request):
	return HttpResponse('heheh')
# Create your views here.
def nazwa(request, nazwa_name_slug):
	context_dict={}
	try:
		nazwa = Nazwa.objects.get(slug=nazwa_name_slug)
		context_dict['nazwa_name'] = nazwa.name
		itemki=Menu_Item.objects.filter(name=nazwa)
		
		context_dict['itemki']=itemki

		context_dict['nazwa']=nazwa
	except Nazwa.DoesNotExist:
		pass
	return render(request, 'ele/nazwa.html')
