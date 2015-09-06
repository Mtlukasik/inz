
from matplotlib import pylab
from pylab import *
import matplotlib.dates as md
import PIL
import PIL.Image
import StringIO
import os
import sqlite3
import numpy as np
def lol(n):
	try:		
		
		conn1=sqlite3.connect('htmlparser.db')
		curs1=conn1.cursor()
		conn=sqlite3.connect('lemp.db')
		curs=conn.cursor()
		
		suma1=0
		cena=[]
		for row in curs1.execute("SELECT * FROM ceny"):
			suma1+=1
	
		for row in curs1.execute("SELECT * FROM ceny"):
			suma1 -= 1
			if (suma1<=n):
				cena.append(float(row[1]))
		kW=[]
		my_ticks=[]		
		suma=0
		for row in curs.execute("SELECT * FROM pomy"):
			suma+=1
		my_xtics=[]
		for row in curs.execute("SELECT * FROM pomy"):
			suma-=1
			if (suma<=n):
				my_ticks.append(str((row[0].split(' ')[1][:5])))
			
				kW.append(float(row[1]))
				
		kW=np.array(kW)
		cena=np.array(cena)
		print kW
		print cena
		m=kW*cena
		print m
	finally:
		pass
lol(6)
