#Practica HTTP - Miguel Angel Fernandez Sanchez

import SimpleHTTPServer	
import SocketServer
from os import curdir, sep, path
  
PORT = 8000	

class HttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):	
    def do_GET(self):	
        print "REQUESTED RESOURCE:", self.path
        fpath = curdir + sep + self.path
        try:
            f = open(fpath)
            fsize = path.getsize(fpath)
        except IOError:
            self. send_error(404, 'File Not Found: %s' % self.path)
        return

        """No concatena en el mismo string el 200 y la cabecera content-type
        aunque es lo mismo porque el manejador o el navegador en el otro
        lado, no va a hacer nada hasta que reciba el ultimo byte"""

        if self.path.endswith(".html"):
            self.send_header("Content-type", "text/html")
        elif self.path.endswith(".txt"):
            self.send_header("Content-type", "text/plain")
        elif self.path.endswith(".jpg"):
            self.send_header("Content-type", "image/jpg")
        elif self.path.endswith(".mp4"):
            self.send_header("Content-type", "video/mp4")
        elif self.path.endswith(".mp3"):
            self.send_header("Content-type", "audio/mp3")
        else:
            self.send_header("Content-type", "application/octet-stream")

        self.end_headers() #Pone un CRLF
        self.wfile.write(f.read())

        #EL SEPARADOR CRLF ES PARTE DEL MENSAJE


httpd = SocketServer.TCPServer(("", PORT), HttpHandler)
print "serving at port", PORT
httpd.serve_forever()
