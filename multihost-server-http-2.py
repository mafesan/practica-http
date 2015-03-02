#Practica HTTP - Miguel Angel Fernandez Sanchez
#Multihost

import SimpleHTTPServer	
import SocketServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
  
PORT = 8000	

class HttpMultisiteHandler(SimpleHTTPRequestHandler):	
    def do_GET(self):
        host = self.headers.getheader('Host')
        self.path = "/" + host + self.path
        Handler.do_GET(self)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), HttpMultisiteHandler)
print "serving at port", PORT
httpd.serve_forever()

"""
¿Sería posible acceder con un navegador estandar
al sitio con nombre cssai1 o cssai2? ¿Como?
