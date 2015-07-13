import os, sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
sys.path.append('/usr/local/lib/python2.7/sqlite3')
import minimalmodbus
import datetime
import time
import sqlite3



"""print "\nEntire database contents:\n"
for row in curs.execute("SELECT * FROM temps"):
    print row

print "\nDatabase entries for the garage:\n"
for row in curs.execute("SELECT * FROM temps WHERE zone='garage'"):
    print row
"""
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instrument.serial.baudrate = 9600
instrument.serial.stopbits = 2
instrument.mode = minimalmodbus.MODE_RTU


def log_data(pomiar3):

    conn=sqlite3.connect('lemp.db')
    curs=conn.cursor()

    curs.execute("INSERT INTO pomy values(datetime('now'), (?))", (pomiar3,))
    

    # commit the changes
    conn.commit()

    conn.close()


#def main():
i=0
while(True):
#przydaloby sie
	if i==100:
		r=open('text.txt','a')
		r.write("udalo zaladowac o " +	str(datetime.datetime.now()) + "\n")
		r.close()
		break #tu wstawic ile rekordow ma byc
	while(True):
		#time.wait(5)
		try:
			pomiar1=instrument.read_register(1, 1)
			pomiar2=instrument.read_register(0, 1)#napiecie*prad
			pomiar3=instrument.read_register(3, 1)#kw
				
			log_data(pomiar3)
			i+=1	
			
			break
		
		except:
		
			continue
	

"""
if __name__ == '__main__':
	try:
		main()

	except KeyboardInterrupt:
		print "przerwano"
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
""""""
pomiar = instrument.read_register(8,1)
print pomiar
"""
