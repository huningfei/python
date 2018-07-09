import time
import socketserver
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn=self.request
        print(conn)
        time.sleep(1)
        conn.send(b'hello')
        time.sleep(1)
        conn.send(b'world')
myserver=socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
myserver.serve_forever()