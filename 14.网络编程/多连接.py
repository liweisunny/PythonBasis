# -*- coding: utf-8 -*-
#到目前为止讨论的服务器解决方案都是同步的：即一次只能连接一个客户机并处理它的请求。如果每个请求只花费很少的时间，比如一个完整的聊天会话，那么同事能处理多个连接就很重要。
#实现方式：分叉（forking）、线程（threading）、以及异步I/O
#分叉：复制当前进程，从当前的执行点继续执行，进程之间完全隔离（有点类似于NET中的应用程序域），缺点：分叉占用资源。客户端太多的时候不好分叉，Windows不支持分叉。
#工作原理：在一个使用分叉的服务器中，每一个客户端连接都利用分叉创造一个子进程（每个分叉出来的进程都需要自己的内存，所以占用资源）。父进程继续监听新的连接，同时子进程处理客户端，当客户端的请求结束时，子进程就退出了，因为分叉的进程是并行运行的，客户端之间不必互相等待。

#线程：轻量级的进程或子进程，所以线程都存在与相同的进程中，共享内存，资源消耗的下降伴随着一个缺陷：因为线程共享内存，就会存在线程安全问题。
'''
#分叉处理
from SocketServer import TCPServer,ForkingMixIn,StreamRequestHandler
class Server(ForkingMixIn,TCPServer):pass
class Handler(StreamRequestHandler):
    def handle(self):
        addr=self.request.getpeername()
        print 'Get connection from',addr
        self.wfile.write('Thank you for connecting')
server=Server(('',125),Handler)
server.serve_forever()


'''
#线程处理
from SocketServer import TCPServer,ThreadingMixIn,StreamRequestHandler
class Server(ThreadingMixIn,TCPServer):pass
class Handler(StreamRequestHandler):
    def handle(self):
        addr=self.request.getpeername()
        print 'Get connection from',addr
        self.wfile.write('Thank you for connecting')
server=Server(('',125),Handler)

server.serve_forever()

print server.socket.recv(1024)