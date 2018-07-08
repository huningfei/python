import time
import socketserver
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):

        self.data=self.request.recv(1024).strip()
        self.data=self.r
        print(self.data)

myserver=socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
myserver.serve_forever()


