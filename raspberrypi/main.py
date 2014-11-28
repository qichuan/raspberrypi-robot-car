import SimpleHTTPServer
import SocketServer
import urlparse
from motor import Motor


PORT = 8000

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    
    def __init__(self, request, client_address, server):
        self.motor = Motor()
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, client_address, server)
        
    def do_GET(self):
        parsedParams = urlparse.urlparse(self.path)
        #queryParsed = urlparse.parse_qs(parsedParams.query)
        
        if parsedParams.path == "/forward":
            self.go_forward()
        elif parsedParams.path == "/backward":
            self.go_backward()
        elif parsedParams.path == "/turnRight":
            self.turn_right()
        elif parsedParams.path == "/turnLeft":
            self.turn_left()
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def go_forward(self):
        self.motor.left_fwd_start()
        self.motor.left_bck_stop()
        self.motor.right_fwd_start()
        self.motor.right_bck_stop()
        self.print_msg("forward")
        
    def go_backward(self):
        self.motor.left_back_start()
        self.motor.left_fwd_stop()
        self.motor.right_bck_start()
        self.motor.right_fwd_stop()
        self.print_msg("backward")
        
    def turn_left(self):
        self.print_msg("turn left")
        
    def turn_right(self):
        self.print_msg("turn right")
        
    def print_msg(self, msg):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(msg)
        self.wfile.close()
        

Motor.initialization()
Handler = MyHandler
SocketServer.allow_reuse_address = True
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
