import urllib2
from bs4 import BeautifulSoup
import lemp
response = urllib2.urlopen('http://www.cenapradu.strefa.pl/').read()

soup = BeautifulSoup(response,"html5lib")

soup2=soup.body.div.div.table.tbody.tr.td.table.tbody.tr.td.table.tbody.tr
#wybor rzedu
i=5
for i in xrange(i):
	soup2=soup2.next_sibling.next_sibling

soup2=soup2.td
#wybor kolumny
m=4
for m in xrange(m):
	soup2=soup2.next_sibling.next_sibling
a=str(soup2.getText())
a=a.split()
b=[]
for i in xrange(len(a[0])):
	if a[0][i]==',':b.append('.')
	else:
		b.append(a[0][i])
b=''.join(b)
b=float(b)
log_data(b,htmlparser.db)