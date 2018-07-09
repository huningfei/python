import socket
sk=socket.socket(type=socket.SOCK_DGRAM)
while True:
    inp=input('>>>')
    if inp=='q':break
    sk.sendto(inp.encode('utf-8'),('127.0.0.1',8899))
    ret=msg,addr=sk.recvfrom(1024)

    print(msg.decode('utf-8'))
    if msg.decode('utf-8') =='q':break
sk.close()