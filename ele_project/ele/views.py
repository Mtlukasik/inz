from django.shortcuts import render
from django.http import HttpResponse
from ele.models import Category
from ele.models import Page
from matplotlib import pylab
from pylab import *
import matplotlib.dates as md
import PIL
import PIL.Image
import StringIO
import os
import sqlite3
import numpy as np
def index(request):#odpowiedzialny za widok glownej strony
    	category_list = Category.objects.all()
    	context_dict = {'categories': category_list}
	return render(request,'ele/index.html',context_dict)
def ostronie(request):
	return HttpResponse('heheh')

def category(request, category_name_slug):
	context_dict={}
	try:
		category = Category.objects.get(slug=category_name_slug)
        	context_dict['category_name'] = category.name
		pages = Page.objects.filter(category=category)
		
		context_dict['pages']=pages

		context_dict['category']=category
	except Nazwa.DoesNotExist:
		pass
	return render(request, 'ele/category.html',context_dict)
def data1(m):
	area = 0.0
	for _ in xrange(0,len(m)-1):
		area += (1.0/6)*(min(float(m[_]),float(m[_+1]))+(1.0/2)*(abs(float(m[_])-float(m[_+1]))))
	
	
	return area
def predata(n):
	n = float(n)
	conn1 = sqlite3.connect('htmlparser.db')
	curs1 = conn1.cursor()
	conn = sqlite3.connect('lemp.db')
	curs = conn.cursor()
		
	a=1		#ta zmienna wyznaczac bedzie co ktory xticks znajdzie sie na labelu
	if n>18:
		m=int(n)
		for _ in xrange(5,m):
			if m%_==0:
				a=_
				break; 
			else: a=n/8.0   # jesli _ jest dzielnikiem n to co tyle probek bedzie olabowane
	else:a=n

	suma1=0
	cena=[]
	for row in curs1.execute("SELECT * FROM ceny"):
		suma1+=1
	
	for row in curs1.execute("SELECT * FROM ceny"):
		suma1 -= 1
		if (suma1<=n):
			cena.append(float(row[1]))
		


	kW=[]
	
	suma=0
	for row in curs.execute("SELECT * FROM pomy"):
		suma+=1
		
	for row in curs.execute("SELECT * FROM pomy"):
		suma-=1
		if (suma<=n):
			
			kW.append(float(row[1]))
				

		
		
	kW=np.array(kW)
	cena=np.array(cena)
	m=kW*cena*0.1
	return m










def graph(request,n):
	try:

		n = float(n)
		conn1 = sqlite3.connect('htmlparser.db')
		curs1 = conn1.cursor()
		conn = sqlite3.connect('lemp.db')
		curs = conn.cursor()
		
		a=1		#ta zmienna wyznaczac bedzie co ktory xticks znajdzie sie na labelu
		if n>18:
			m=int(n)
			for _ in xrange(5,m):
				if m%_==0:
					a=_
					break; 
				else: a=n/8.0   # jesli _ jest dzielnikiem n to co tyle probek bedzie olabowane
		else:a=n

		suma1=0
		cena=[]
		for row in curs1.execute("SELECT * FROM ceny"):
			suma1+=1
	
		for row in curs1.execute("SELECT * FROM ceny"):
			suma1 -= 1
			if (suma1<=n):
				cena.append(float(row[1]))
		


		kW=[]
		my_xticks=[]		
		suma=0
		for row in curs.execute("SELECT * FROM pomy"):
			suma+=1
		my_xtics=[]
		for row in curs.execute("SELECT * FROM pomy"):
			suma-=1
			if (suma<=n):
				
				if suma%(n/a)==0:	
					if n>160:
						my_xticks.append(str((row[0][:16])))
					else:
						my_xticks.append(str((row[0].split(' ')[1][:5])))
				else:
					my_xticks.append(str(' '))
			
				kW.append(float(row[1]))
				

		
		
		kW=np.array(kW)
		cena=np.array(cena)
		m=kW*cena*0.1

		x=np.linspace(0,n,n+1)
		
		
		


		
		gcf().subplots_adjust(bottom=0.20)
		plt.xticks(x,my_xticks,rotation=25)
		plot(x,m,linewidth=2)
		gcf().subplots_adjust(bottom=0.15)
		ylabel('kW * PLN')
		if n>140:
			tekst='Pokazuje ostatnie %d dni'% ((n-n%148)/148)
		else:
			tekst='Pokazuje ostatnie %d h'% ((n-n%6)/6)
		title(tekst)
		grid(True)
		
		buffer = StringIO.StringIO()
		canvas = pylab.get_current_fig_manager().canvas
		canvas.draw() #zaladowanie informacji
		graphIMG=PIL.Image.fromstring("RGB",canvas.get_width_height(),canvas.tostring_rgb())
		graphIMG.save(buffer,"PNG")
		pylab.close()
		
	finally:
		pass
	return HttpResponse(buffer.getvalue(), content_type="image/png")

def graphic(request,n):
	context={}
	context['boldmessage'] = n
	context['wydatek']=round(data1(predata(n)),2)
	return render(request,'ele/graphic.html',context)

	
