import SimpleHTTPServer	
import SocketServer	
  
PORT = 8000	

class HttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):	
  def do_GET(self):	
  	print "REQUESTED RESOURCE:",self.path
  
httpd =	SocketServer.TCPServer(("", PORT), HttpHandler)  
print "serving at port", PORT 
httpd.serve_forever()
 
