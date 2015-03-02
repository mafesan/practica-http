import SimpleHTTPServer	
import SocketServer	
  
PORT = 8000	

class HttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):	
    def do_GET(self):	
        print "REQUESTED RESOURCE:", self.path
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')		
            self.end_headers()	
            self.wfile.write("<html><body>ROOT</body></html>")
        else:
            self.send_error(404, 'Resource not found: %s'  % self.path)
  
httpd =	SocketServer.TCPServer(("", PORT), HttpHandler)  
print "serving at port", PORT 
httpd.serve_forever()
 
