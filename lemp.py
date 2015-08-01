import os, sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
sys.path.append('/usr/local/lib/python2.7/sqlite3')
import minimalmodbus
import datetime
import time
import sqlite3


def log_data(pomiar3):

    conn=sqlite3.connect('lemp.db')
    curs=conn.cursor()

    curs.execute("INSERT INTO pomy values(datetime('now'), (?))", (pomiar3,))
    

    # commit the changes
    conn.commit()

    conn.close()


def main():

	instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
	instrument.serial.baudrate = 9600
	instrument.serial.stopbits = 2
	instrument.mode = minimalmodbus.MODE_RTU



	while(True):

		try:	
			r=open('text.txt','a')
			r.write("zaczynam " + "\n")
			r.close()
			pomiar1=instrument.read_register(1, 1)
			pomiar2=instrument.read_register(0, 1)#napiecie*prad
			pomiar3=instrument.read_register(3, 1)#kw
				
			log_data(pomiar3)
			r=open('text.txt','a')
			r.write("udalo zaladowac o " +	str(datetime.datetime.now()) + "\n")
			r.close()	
			
			break
		
		except:
		
			continue
	


if __name__ == '__main__':
	
	main()


