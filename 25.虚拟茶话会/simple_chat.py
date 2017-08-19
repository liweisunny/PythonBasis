# -*- coding:utf-8 -*-
from asyncore import dispatcher
from asynchat import async_chat
import socket,asyncore
PORT=5555
NUM=5
NAME='TestChat'
class ChatSession(async_chat):
    def __init__(self,server,sock):
        async_chat.__init__(self,sock)
        self.server=server
        self.set_terminator('\r\n')
        self.data=[]
        #问候用户
        self.push('Welcome to %s \r\n'%self.server.name)
    def collect_incoming_data(self, data):
        self.data.append(data)
    def found_terminator(self):
        # 如果发现一个完整对象，也就意味着读入了一个完整的行，将其广播给每个用户
        line=''.join(self.data)
        self.data=[]
        self.server.broadcast(line)
    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)

class ChatServer(dispatcher):
    '''
    接受连接并且产生单个会话的类，它还会处理到其他会话的广播
    '''
    def __init__(self,port,name):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字，
        self.set_reuse_addr() #确保服务器在没有正确关闭的情况下重用同一个地址，确切的说是端口号；如果不进行调用服务重启前可能需要等一会或者需要更改端口号，因为你的程序可能无法正确通知操作系统用完了某个端口号。
        self.bind(('', port))  # 绑定主机名和端口，''表示本地主机
        self.listen(NUM)  # 监听链接，上限5个
        self.name=name
        self.sessions=[]
    def disconnec(self,session):
        self.sessions.remove(session)
    def broadcast(self,line):
        for session in self.sessions:
            session.push(line+'\r\n')
    def handle_accept(self):
        conn,addr=self.accept()
        self.sessions.append(ChatSession(self,conn))
if __name__=='__main__':
    s=ChatServer(PORT,NAME)
    try:
        asyncore.loop() #启动服务，开启循环监听
    except KeyboardInterrupt:
        pass