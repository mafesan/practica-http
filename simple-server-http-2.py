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

        self.send_response(200)
        self.end_headers()
        self.wfile.write(f.read())
  
httpd =	SocketServer.TCPServer(("", PORT), HttpHandler)  
print "serving at port", PORT 
httpd.serve_forever()
