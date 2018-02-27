import time
import serial
from datetime import datetime
ser = serial.Serial ("/dev/serial0")    #Open named port
ser.baudrate = 9600                     #Set baud rate to 9600
#from neo6 import GpsNeo6
#gps=GpsNeo6(port="/dev/serial0",debit=9600,diff=2) #diff is difference between utc time en local time
#gps.traite()
#print(gps)  # print all info
longitude = 0   #first
latitude = 0    #second
alttude = 0

try:
    while 1:
        #ser.write()
        data = ser.readline(-1)  # Read ten characters from serial port to data
        dataSplited = data.split(',')
        '''if dataSplited[0] == "$GPGLL":
            print "----------------------------GPGLL----------------------------------"
            latitude = float(dataSplited[1]) / 100
            longitude = float(dataSplited[3])/100
            heure = datetime.strptime(dataSplited[5], '%H%M%S.%f')
            print data
            print "--- --- --- --- --- --- --- --- " + str(heure)
            print str(longitude) + "N " + str(latitude) + "E"'''

        '''if dataSplited[0] == "$GPGGA":
            print "----------------------------GPGGA----------------------------------"
            latitude = float(dataSplited[2]) / 100
            longitude = float(dataSplited[4]) / 100
            altitude = float(dataSplited[9])
            heure = datetime.strptime(dataSplited[1], '%H%M%S.%f')
            print data
            print "--- --- --- --- --- --- --- --- " + str(heure)
            print str(latitude) + dataSplited[3] + " " + str(longitude) + dataSplited[5] + " " + str(altitude) + "M"'''
        print data
        #gps.traite()
        #print(gps.latitude, gps.longitude)
finally:
    ser.close()