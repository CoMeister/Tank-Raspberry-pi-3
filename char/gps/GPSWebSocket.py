#sudo gpsd /dev/serial0 -F /var/run/gpsd.sock
import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import tornado.options
import threading

from gps import *
import time
import os

gpsd = None
gpsd = gps(mode=WATCH_ENABLE)

print "start gps"
#--------------WebSocket--------------

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    threads = []

    def check_origin(self, origin):
        return True

    def open(self):	#action a l'ouverture de session
        print "Connection oppened"
        #self.write_message("Connection opened")
        self.send_gps_data()
        '''t = threading.Thread(target=self.send_gps_data)  #threading
        self.threads.append(t)
        t.start()'''

    def on_message(self, message):	#Que faire si l'on recoit un message
        self.write_message(message)
        if message == "gpsLoc":
            time.sleep(1)
            self.send_gps_data()
        print message

    def on_close(self):			#que faire a la fermeture de session
        print "Connection closed"
        #self.close_event.set()

    def sendData(self, data):
	    self.write_message(data)

    def send_gps_data(self):
        try:
            while 1:
                gpsd.next()
                print "Coordonees :     " + str(gpsd.fix.latitude) + " " + str(gpsd.fix.longitude)
                '''print "Time :           " + gpsd.utc
                print "Test :           " + str(gpsd.fix.epx)'''
                self.write_message(str(gpsd.fix.latitude) + ";" + str(gpsd.fix.longitude))e
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):  # when you press ctrl+c
            print "\nKilling Thread..."
            print "Done.\nExiting."


app = tornado.web.Application(handlers=[(r"/", WebSocketHandler)])

#-------------------------------------

try:
    tornado.options.parse_command_line()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8888)
    # main_loop = tornado.ioloop.IOLoop.instance()
    tornado.ioloop.IOLoop.instance().start()
except (KeyboardInterrupt, SystemExit):  # when you press ctrl+c
    print "\nKilling Thread..."
    print "Done.\nExiting."
