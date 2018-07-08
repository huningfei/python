import socket
sk=socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',8899))
while True:
    msg,addr=sk.recvfrom(1024)
    print(msg.decode('utf-8'),addr)
    inp=input('>>>:')
    if inp=='q':break
    sk.sendto(inp.encode('utf-8'),addr)
    #print(msg)
sk.close()