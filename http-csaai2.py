#Practica HTTP - CSAAI -2
#Miguel Angel Fernandez Sanchez

import  SimpleHTTPServer
import  SocketServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

PORT  =  8000

class HttpMultisiteHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(self):
            host = self.headers.getheader('Host')
            self.path = "/" + str(host) + self.path
            Handler.do_GET(self)

Handler  =  SimpleHTTPServer.SimpleHTTPRequestHandler
httpd  =  SocketServer.TCPServer(("",  PORT),  HttpMultisiteHandler)
print  "serving  at  port",  PORT
httpd.serve_forever()
