#sudo gpsd /dev/serial0 -F /var/run/gpsd.sock
from gps import *
import time
import os

#os.system('sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock')        #if no script at launch

gpsd = None

gpsd = gps(mode=WATCH_ENABLE)

try:
    while True:
        os.system('clear')
        gpsd.next()
        print "Coordonees :     " + str(gpsd.fix.latitude) + " " + str(gpsd.fix.longitude)
        print "Time :           " + gpsd.utc
        print "Test :           " + str(gpsd.fix.epx)
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):  # when you press ctrl+c
    print "\nKilling Thread..."
    print "Done.\nExiting."
