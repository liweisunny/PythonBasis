# -*- coding: utf-8 -*-
#通过网络访问文件
#打开远程文件
from  urllib import  urlopen
webpage=urlopen('http://www.python.org')#返回一个类文件对象,支持close 、read 、readline、 readlines 方法
import re
text=webpage.read()
m=re.search('<a href="([^"]+)".*?>about</a>',text,re.IGNORECASE)
print m.group(1)
#获取远程文件：下载文件并在本地文件中存储一个副本
from urllib import  urlretrieve
urlretrieve('http://www.python.org')
urlretrieve('http://www.python.org','D:\\python_webpage.html')#指定文件存储路径和文件名
#说明：如果没有指定文件名，文件就会放在临时位置，可以用open函数操作它，要清理临时文件以节省磁盘空间可以用urlcleanup函数