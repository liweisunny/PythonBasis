# -*- coding: utf-8 -*-
import socket,select
s=socket.socket()
host=socket.gethostname()
port=125
s.bind((host,port))
s.listen(5)#
inputs=[s]
while True:
    rs,ws,es=select.select(inputs,[],[])
    for r in rs:
        if r is s:#判断是否是套接字
            c,addr=s.accept()
            print 'Go connection from',addr
            c.send('Thank You For Connecting')
            inputs.append(c)
        else:
            try:
                data=r.recv(1024)
            except socket.error:
                disconnected=True
            if disconnected:
                print r.getpeername(),'disconnected'
            else:
                print data
