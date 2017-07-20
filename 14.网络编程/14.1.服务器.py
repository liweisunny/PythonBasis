# -*- coding: utf-8 -*-
import socket
s=socket.socket()#创建套接字
host=socket.gethostname()#获取当前主机名
port=125#端口号
s.bind((host,port))#绑定
s.listen(5)
#print s.recv(1024)
while True:
    client,adress=s.accept()
    print '%s connect Sucess!'%client
    client.send('Thank You For Connecting')
    print client.recv(1024)
    client.close()

    