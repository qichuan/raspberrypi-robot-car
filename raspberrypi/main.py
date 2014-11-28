import SimpleHTTPServer
import SocketServer
import urlparse
# import motor


PORT = 8000

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    # def __init__(self):
    # self.motor = Motor()
    def do_GET(self):
        parsedParams = urlparse.urlparse(self.path)
        queryParsed = urlparse.parse_qs(parsedParams.query)
        
        if parsedParams.path == "/forward":
            self.go_forward(queryParsed)
        
        # request is either for a file to be served up or our test
        if parsedParams.path == "/test":
            self.processMyRequest(queryParsed)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
            
    def processMyRequest(self, query):
        self.send_response(200)
        self.send_header('Content-Type', 'application/xml')
        self.end_headers()
        self.wfile.write("<?xml version='1.0'?>")
        self.wfile.write("<sample>Some XML</sample>")
        self.wfile.close()

    def go_forward(self, query):
#        # self.motor.right_fwd_start()
        self.send_response(200)
        self.send_header('Content-Type', 'application/xml')
        self.end_headers()
        self.wfile.write("<?xml version='1.0'?>")
        self.wfile.write("<command>forward</command>")
        self.wfile.close()

Handler = MyHandler
SocketServer.allow_reuse_address = True
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
