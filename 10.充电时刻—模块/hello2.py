# -*- coding: utf-8 -*-
#作为模块导入--函数
def hello(msg):
    print msg
def test(msg):#将测试代码放入 到函数里面，这样程雪会更加灵活，因为这样写外部也可以调用测试代码
    hello(msg)
#测试函数是否能够正常执行
#hello('123')#直接这样写的话在导入模块hello2的时候这个函数就会被执行一次这不是我们想要的，所以使用__name__变量
if  __name__=='__main__':
    test('123')