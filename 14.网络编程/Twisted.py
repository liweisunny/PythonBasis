# -*- coding: utf-8 -*-
'''
#版本一
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
class SimpleLogger(Protocol):#自定义协议类
    def connectionMade(self):#接收到客户端连接的时候被调用
        print 'Get connection from',self.transport.client
    def connevtionLost(self,reason):#客户端断开连接的时候被调用
        print  self.transport.client,'disconnected'
    #接受客户端发送过来的数据
    def dataReceived(self,data):#这个方法一次性只输出一个字符
        print data
factory=Factory()
factory.protocol=SimpleLogger
reactor.listenTCP(1234,factory)#监听客户端链接
reactor.run()#启动服务器
'''




#版本二
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LinReceiver

class SimpleLogger(LinReceiver):#自定义协议类
    def connectionMade(self):#接收到客户端连接的时候被调用
        print 'Get connection from',self.transport.client
    def connevtionLost(self,reason):#客户端断开连接的时候被调用
        print  self.transport.client,'disconnected'
    #接受客户端发送过来的数据
    def lineReceived(self,line):#这个一次输出一行
        print line
factory=Factory()
factory.protocol=SimpleLogger
reactor.listenTCP(1234,factory)#监听客户端链接
reactor.run()#启动服务器