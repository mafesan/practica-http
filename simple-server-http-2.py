import SimpleHTTPServer	
import SocketServer	
  
PORT = 8000	

class HttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):	
    def do_GET(self):	
        print "REQUESTED RESOURCE:", self.path
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')		
        self.end_headers()	
        self.wfile.write("<html><body>Tiny server response</body></html>")
  
httpd =	SocketServer.TCPServer(("", PORT), HttpHandler)  
print "serving at port", PORT 
httpd.serve_forever()
 
