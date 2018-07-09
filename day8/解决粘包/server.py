import socket
import struct
sk=socket.socket()
sk.bind(('127.0.0.1',8090))
sk.listen()
conn,addr=sk.accept()
inp=input('>>>:').encode('utf-8')
inp_len=len(inp)#计算用户输入的长度
bytes_msg=struct.pack('i',inp_len)#将数字转换成固定的bytes
conn.send(bytes_msg) #先发送报头的长度4个bytes
conn.send(inp)#在发送报头的字节格式
conn.send(b'alex sb')#最后发送真实内容的字节格式
conn.close()
sk.close()

