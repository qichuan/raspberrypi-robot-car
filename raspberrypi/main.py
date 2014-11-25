import SimpleHTTPServer
import SocketServer
import urlparse
import motor


PORT = 8080

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

   def __init__(self):
       self.motor = Motor()

   def do_GET(self):

       # Parse query data & params to find out what was passed
       parsedParams = urlparse.urlparse(self.path)
       queryParsed = urlparse.parse_qs(parsedParams.query)
       
       if parsedParams.path=="/forward":
          self.go_forward()

       # request is either for a file to be served up or our test
       else if parsedParams.path == "/test":
          self.processMyRequest(queryParsed)
       else:
          # Default to serve up a local file 
          SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self);
          
   def go_forward(self):
       self.motor.right_fwd_start()
       self.send_response(200)
       self.send_header('Content-Type', 'application/html')
       self.end_headers()
       self.wfile.write("forward");
       self.wfile.close();
          
   def processMyRequest(self, query):

       self.send_response(200)
       self.send_header('Content-Type', 'application/xml')
       self.end_headers()

       self.wfile.write("<?xml version='1.0'?>");
       self.wfile.write("<sample>Some XML</sample>");
       self.wfile.close();

Handler = MyHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()