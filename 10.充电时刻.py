# -*- coding: utf-8 -*-

# 10.1 模块：为了将代码可重用，请将其模块化！

# 10.1.1导入系统模块
import math
print math.sin(0)

# 10.1.2导入自己编写的模块
import sys
sys.path.append('E:\Python\练习\PythonBasis')

import hello
import hello #再次导入模块就什么都不会发生了
# 为什么这次没用了?因为导人模块并不意味着在导入时执行某些操作(比如打印文本)。它们主要用于定义，比如变量、函数和类等。此外，因为只需要定义这些东西一次，导人模块多次和导人一次的效果是一样的。
import hello2 #导入模块hello2
hello2.hello('函数--模块导入')

# 10.1.3让模块更可用

# 1将模块放到正确的位置
import sys,pprint
pprint.pprint(sys.path)#打印出的这些目录都可以存放模块，但是site-packages这个目录最佳，因为他就是用来做这些事情的。将模块放入到类似于这样的目录里，所有程序就都可以导入了

sys.path.append('D:\\Python27\\lib\\site-packages')
import site_hello
site_hello.hello('site-packages目录下的模块导入成功！！')



