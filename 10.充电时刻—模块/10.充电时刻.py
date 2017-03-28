# -*- coding: utf-8 -*-
# 10.1 模块：为了将代码可重用，请将其模块化！

# 10.1.1导入系统模块
import math
print math.sin(0)

# 10.1.2导入自己编写的模块
import sys
sys.path.append('E:\Python\练习\PythonBasis')

# 为什么这次没用了?因为导人模块并不意味着在导入时执行某些操作(比如打印文本)。它们主要用于定义，比如变量、函数和类等。此外，因为只需要定义这些东西一次，导人模块多次和导人一次的效果是一样的。
import hello2  #导入模块hello2
hello2.hello('函数--模块导入')

# 10.1.3让模块更可用

# 1将模块放到正确的位置
import sys,pprint
pprint.pprint(sys.path)#打印出的这些目录都可以存放模块，但是site-packages这个目录最佳，因为他就是用来做这些事情的。将模块放入到类似于这样的目录里，所有程序就都可以导入了

sys.path.append('D:\\Python27\\lib\\site-packages')
import site_hello
site_hello.hello('site-packages目录下的模块导入成功！！')

# 10.1.4 包
# 为了组织好模块，你可以将它们分组为包(package)。包基本上就是另外一类模块，有趣的地方就是它们能包含其他模块。
# 当模块存储在文件中时(扩展名.Py)，包就是模块所在的目录。为了让Python将其作为包对待，它必须包含一个命名为__init__.py的文件(模块)。如果将它作为
# 普通模块导入的话，文件的内容就是包的内容。比如有个名为 Constants包，文件Constants/__init__.py包括语句PI=3.14，那么你可以像下面这么做:
import Constants
print Constants.Pi

# 10.2 探究模块
#例①  导入copy模块，以此为例介绍
import copy

#dir函数： 查看模块包含的内容可以使用dir函数，它会将对象(以及模块的所有函数、类、变量等)的所有特性列出。如果想要打印出dir(copy)的内容，你会看到一长串名字(试试看)。
# 一些名字以下划线开始一一暗示(约定俗成)它们并不是为在模块外部使用而准备的。所以让我们用列表推导式过滤掉它们:
print [n for n in dir(copy) if not n.startswith('_')]

#__all__变量：这个变量包含一个列表，该列表与我之前通过列表推导式创建的列表很类似—除了这个列表在模块本身中被设置。我们来看看它都包含哪些内容:

print copy.__all__

# 说明：这个变量在copy模块内部被设置：__all__=['Error', 'copy', 'deepcopy']；它定义了模块的公有接口。更准确的说，它告诉解释器：从模块导入所有名字代表什么含义，
# 因此，如果如果使用如下代码： 'from copy import  * ' 那么你只能使用__all__变量中的三个函数，如果你要导入其它函数（如：PyStringMap），你就得显示地实现，
# 或者导入copy然后使用copy.PyStringMap,或者使用 from copy import PyStringMap。
# 在编写模块的时候，像设置__all__这样的技术是相当有用的。因为模块中可能会有一大堆其他程序不需要或不想要的变量、函数和类，__all__会“客气地”将它们过滤了出去。
# 如果没有设置__all__，用import* 语句默认将会输出模块中所有不以下划线开头的全局名称。

# help函数
print help(copy)
print help(copy.copy)
print copy.copy.__doc__

# 文档
print range.__doc__

#使用源代码

print copy.__file__#这个是输出copy模块源代码文件的路径，查看以.py结尾的文件

# 10.3 标准库

# 10.3.1 sys 这个模块能让你访问与python解释器联系紧密的变量和函数

# ①变量sys.argv包括传递到Python解释器的参数，包括脚本名称。
#使用python解释器执行sys_argv.py脚本

# ② 函数sys.exit可以退出当前程序(如果在try/finally块中调用，finally子句的内容仍然会被执行翁)。

# ③ 映射sys.modules将模块名映射到实际存在的模块上，它只应用于目前导入的模块。

# ④ sys.path它是一个字符串列表，其中的每个字符串都是一个目录名，在import语句执行时，解释器就会从这些目录中查找模块。

# ⑤ sys.platform模块变量(它是个字符串)是解释器正在其上运行的“平台”名称。它可能是标识操作系统的名字(比如sunos5或者win32 )，也可能标识其他种类的平台，如果你运行Jython的话，就是.lava虚拟机(比如：Java1.4.0 )。

# ⑥ sys.stdin, sys.stdout和sys.stderr模块变量是类文件流对象。它们表示标准UNIX概念中的标淮输入、标准输出和标准错误。简单来说卫尹1110I1利用sys.stdin获得输人(比如用于函数input和raw_input中的输入)，利用sys.stdout输出。


# 10.3.2 os 这个模块为你提供了访问多个操作系统服务的功能。
import os
# 1. os.environ映射包含本章前面讲述过的环境变量。比如要访问系统变量P丫丁HONPATH，可以使用表达式os.environ['PYTHONPATH']。这个映射也可以用来更改系统环境变量，不过并非所有系统都支持。
print os.environ['PYTHONPATH']

# 2. os.system函数用于运行外部程序。也有一些函数可以执行外部程序，包括execv，它会退出Python解释器，并且将控制权交给被执行程序。还有popen，它可以创建与程序连接的类文件。
#例 启动系统中安装的谷歌浏览器

# ①.UNIX系统中的调用方式：(假设/user/bin/firebox目录下安装了浏览器)
#os.system('/user/bin/firebox')

# ②.windows中的调用方式是：
#os.system(r'C:\"Program Files (x86)"\"Google\Chrome"\"Application"\chrome.exe')#注意每个目录下的双引号
# 注意，我很仔细地将Program Files和Google\Chrome以及Application放入引号中，不然DOS(它负责处理这个命令)就会在空格处停下来(对于在PYTHONPATH中设定的目录来说，这点也同样重要)。
# 同时，注意必须使用反斜线，因为DOS会被正斜线弄糊涂。如果运行程序，你会注意到浏览器会试图打开叫做Files"\…的网站一也就是在空格后面的命令部分。
# 另一方面，如果试图在IDLE中运行该代码，你会看到DOS窗口出现了，但是没有启动浏览器并没有出现，除非关闭DOS窗口。总之，使用以上代码并不是完美的解决方法。
# 另外一个可以更好地解决问题的函数是Windows特有的函数：os.startfile:
#os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
# 可以看到，os.startfile接受一般路径，就算包含空格也没问题(也就是不用像在os.system例子中那样将Program Fiels放在引号中)。
# 注意，在Windows中，由os.system(或者os.startfile)启动了外部程序之后，Python程序仍然会继续运行，而在UNIX中，程序则会中止，等待os.system命令完成。
#更好的解决方案
import webbrowser #该模块的open函数可以自动启动web浏览器并打开指定的url
#webbrowser.open('http:\\www.python.org')#如果url=""会打开当前项目路径

# 3. os.sep模块变量是用于路径名中的分隔符。UNIX(以及Mac OS X中命令行版本的Python )中的标准分隔符是“/"，Windows中的是“\\"(即Python针对单个反斜线的语法)，而Mac OS中的是“:”(有些平台上，os.altsep包含可选的路径分隔符，比如Windows中的”/“)。
#    你可以在组织路径的时候使用os.pathsep,就像在PYTHONPATH中一样。pathsep用于分割路径名:UNIX(以及Mac OS X中的命令行版本的Python )使用“:”，Windows使用“;"，Mac OS使用“::”。

# 4. 模块变量os.linesep用于文本文件的字符串分隔符。UNIX中(以及Mac OS X中命令行版本的Python)为一个换行符(\n) , Mac OS中为单个回车符(\r)，而在Windows中则是两者的组合( \r\n )。

# 5. urandom函数使用一个依赖于系统的“真”(至少是足够强度加密的)随机数的源。如果正在使用的平台不支持它，你会得到NotImplementedError异常。


# 10.3.3 fileinput模块

# 1.fileinput.input是其中最重要的函数。它会返回能够用于for循环遍历的对象。如果不想使用默认行为(fileinput查找需要循环遍历的文件)，那么可以给函数提供(序列形式的)一个或多个文件名。
# 你还能将inplace参数设为真值(inplace=True)以进行原地处理。对于要访问的每一行，需要打印出替代的内容，以返回到当前的输入文件中。在进行原地处理的时候，可选的backup参数将文件名扩展备份到通过原始文件创建的备份文件中。

# 2. fileinput.filename函数返回当前正在处理的文件名(也就是包含了当前正在处理的文本行的文件)。

# 3. fileinput.lineno返回当前行的行数。这个数值是累计的，所以在完成一个文件的处理并且开始处理下一个文件的时候，行数并不会重置，而是将上一个文件的最后行数加1作为计数的起始。

# 4. fileinput.filelineno函数返回当前处理文件的当前行数。每次处理完一个文件并且开始处理下一个文件时，行数都会重置为1，然后重新开始计数。

# 5. fileinput.isfirstline函数在当前行是当前文件的第一行时返回真值，反之返回假值。

# 6. fileinput.isstdin函数在当前文件为sys.stdin时返回真值，否则返回假值。

# 7.fileinput.nextfile函数会关闭当前文件，跳到下一个文件，跳过的行并不计。在你知道当前文件已经处理完的情况下，这个函数就比较有用了——比如每个文件都包含经过排序的单词，
# 而你需要查找某个词。如果已经在排序中找到了这个词的位置，那么你就能放心地跳到下一个文件了。

# 8. fileinput.close函数关闭整个文件链，结束迭代。

# 10.3.4 集合、堆、双端队列
# 1.集合 set
print set(range(10)) #set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#集合是由序列（或者其他可迭代对象）构建的。它们主要用于检查成员资格，因此副本是被忽略的：
print set([0,1,2,3,0,1,2,3,4,5])#set([0, 1, 2, 3, 4, 5])
#和字典一样，集合元素的顺序是随意的，因此我们不应该以元素的顺序作为依据进行编程
print set(['fee','fie','foe','fee'])#set(['foe', 'fee', 'fie'])
#集合操作
#①求两个集合的并集，使用union方法或者使用运算符“|”：
a=set([1,2,3])
b=set([2,3,4])
print a.union(b) #set([1,2,3,4])
print a|b        #set([1,2,3,4])

#②求两个集合的交集：intersection、&
print a.intersection(b)#set([2, 3])
print a&b              #set([2, 3])

#③判断子集、父集
c=a&b
print c.issubset(a)#判断c是否是a的子集
print c<=a #True
print c.issuperset(a)#判断c是否是a的超集
print  c>=a #False

#④差集
a.difference(b)#set([1]) a与b的差集 = a-b
print a-b

#⑤对称差集
print a.symmetric_difference(b)#set([1,4])
print b.symmetric_difference(a)#set([1,4])
print a^b#set([1,4])
print b^a#set([1,4])

# copy 返回一个浅复制
print a.copy()
print a.copy() is a

#说明：集合是可变的，所以不能用作字典中的键。另外一个问题就是集合本身只能包含不可变（可散列的）值，所以也就不能包含其他集合，在实际当中，集合的集合很是常用，所以这就是个问题了.。
# 幸好嗨哟个frozenset类型，用于代表不可变（可散列）的集合
#例
a=set(range(5))
b=set(range(2,5))
#a.add(b)#报错
a.add(frozenset(b))#frozenset构造函数创建给定集合的副本
print a

#
myset=[]
for i in range(10):
    myset.append(set(range(i,i+5)))
print reduce(set.union,myset)

#2.堆
#堆(heap)，它是优先队列的一种。使用优先队列能够以任意顺序增加对象，并且能在任何时间(可能在增加对象的同时)找到(也可能是移除)最小的元素，也就是说它比用于列表的min方法要有效率得多。
#事实上，Python中并没有独立的堆类型—只有一个包含一些堆操作函数的模块，这个模块叫做heapq (q是queue的缩写，即队列)，包括6个函数。

#① heappush函数用于增加堆的项。注意，不能将它用于任何之前讲述的列表中—它只能用于通过各种堆函数建立的列表中。原因是元素的顺序很重要(尽管看起来是随意排列，元素并不是进行严格排序的)。
#例
from heapq import *
from random import shuffle
data=range(10)
shuffle(data)#将序列的所有元素随机排序。shuffle()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。返回随机排序后的序列。
heap=[]
for n in data:
    heappush(heap,n)
print heap
heappush(heap,0.5)
print heap
# 元素的顺序并不像看起来那么随意。它们虽然不是严格排序的，但是也有规则的:位于i位置上的元素总比i//2位置处的元素大(反过来说就是i位置处的元素总比2*i以及2*i+1位置处的元素小)。这是底层堆算法的基础，而这个特性称为堆属性(heap property)。

#② heappop函数弹出最小的元素。一般来说都是在索引0处的元素，并且会确保剩余元素中最小的那个占据这个位置(保持刚才提到的堆属性)。一般来说，尽管弹出列表的第一个元素并不是很有效率，但是在这里不是问题，因为heappop在“幕后”会做一些精巧的移位操作:
print heappop(heap)#0
print heap
print heappop(heap)#0.5
print heap
print heappop(heap)#1

#③ heapify函数使用任意列表作为参数，并且通过尽可能少的移位操作，将其转换为合法的堆(事实上是应用了刚才提到的堆属性)。如果没有用heappush建立堆，那么在使用heappush和heappop前应该使用这个函数。
#例
heap=[5,6,3,8,2,9,4,7,0,1]
heapify(heap)
print heap

#④ heapreplace函数不像其他函数那么常用。它弹出堆的最小元素，并且将新元素推入。这样做比调用heappop之后再调用heappush更高效。
#例
print heap
print heapreplace(heap,10)
print heap

#补充：heapq模块中剩下的两个函数nlargest(n,iter)和nsmallest(n,iter)分别用来寻找任何可迭代对象iter中第n大或第n小的元素。你可以使用排序(比如使用sorted函数)和分片来完成这个工作，但是堆算法更快而且更有效地使用内存(还有一个没有提及的优点:更易用)。

# 3.双端队列
# 双端队列(Double-ended queue，或称deque)在需要按照元素增加的顺序来移除元素时非有用。Python 2.4增加了collections模块，它包括deque类型。
# 双端队列通过可迭代对象(比如集合)创建，而且有些非常有用的方法，如下例所示:
from collections import deque
q=deque(range(5))
print q
q.append(5)
q.appendleft(6)
print q
print q.pop()#5
print q.popleft()#6
print q
q.rotate(3)#无返回值，将每个元素向右移3位，循环移动
print q
q.rotate(-1)#将每个元素向左移1位，循环移动
print q
#说明：双端队列好用的原因是它能够有效地在开头(左侧)增加和弹出元素，这是在列表中无法实现的。
# 除此之外，使用双端队列的好处还有:能够有效地旋转(rotate )元素(也就是将它们左移或右移，使头尾相连)。
# 双端队列对象还有extend和extendleft方法，extend和列表的extend方法差不多，extendleft则类似于appendleft。注意，extendleft使用的可迭代对象中的元素会反序出现在双端队列中。

# 10.3.5 time模块
# time模块所包括的函数能够实现以下功能:获得当前时间、操作时间和日期、从字符串读取时间以及格式化时间为字符串。
# 说明：在Python中，通常有这几种方式来表示时间：1）时间戳(从新纪元开始计算的秒数) 2）格式化的时间字符串 3）元组（struct_time）共九个元素。由于Python的time模块实现主要调用C库，所以各个平台可能有所不同。
# UTC（Coordinated Universal Time，世界协调时）亦即格林威治天文时间，世界标准时间。在中国为UTC+8。DST（Daylight Saving Time）即夏令时。
# 时间戳（timestamp）的方式：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。返回时间戳方式的函数主要有time()，clock()等。
# 元组（struct_time）方式：struct_time元组共有9个元素，返回struct_time的函数主要有gmtime()，localtime()，strptime()。
import time
# ①time.localtime([secs])：将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
print time.localtime()#time.struct_time(tm_year=2017, tm_mon=3, tm_mday=18, tm_hour=9, tm_min=24, tm_sec=37, tm_wday=5, tm_yday=77, tm_isdst=0)
# ②time.gmtime([secs])：和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。
print time.gmtime()#time.struct_time(tm_year=2017, tm_mon=3, tm_mday=18, tm_hour=1, tm_min=26, tm_sec=50, tm_wday=5, tm_yday=77, tm_isdst=0)
# ③time.time()：返回当前时间的时间戳
print time.time()#1489800410.56
# ④time.mktime(t)：将一个struct_time转化为时间戳。
print time.mktime((2017, 3, 18, 1, 26, 50, 5, 77, 0))#必须是九个  1489771610.0
print time.mktime(time.localtime())#1489800614.0
# ⑤time.sleep(secs)：线程推迟指定的时间运行。单位为秒。
#time.sleep(2)
print '.....2秒后'
# ⑥time.clock()：这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间戳）。而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。（实际上是以WIN32上QueryPerformanceCounter()为基础，它比毫秒表示更为精确）
#time.sleep(1)
print "clock1:%s" % time.clock()
#time.sleep(1)
print "clock2:%s" % time.clock()
#time.sleep(1)
print "clock3:%s" % time.clock()
#说明：其中第一个clock()输出的是程序运行时间第二、三个clock()输出的都是与第一个clock的时间间隔
# ⑦time.asctime([t])：把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。如果没有参数，将会将time.localtime()作为参数传入。
print time.asctime()#Sat Mar 18 09:35:57 2017
print time.asctime((2017, 3, 30, 1, 26, 50, 5, 77, 0))#Sat Mar 30 01:26:50 2017
# ⑧time.ctime([secs])：把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。
print time.ctime()#Sat Mar 18 09:41:07 2017
print time.asctime(time.localtime())#Sat Mar 18 09:43:39 2017
print time.ctime(time.time())#Sat Mar 18 09:41:07 2017
print time.ctime(189800614.0)#Wed Jan 07 02:23:34 1976
# ⑨time.strftime(format[, t])：把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出。
print time.strftime('%Y-%m-%d %X',time.localtime())#2017-03-18 09:48:07
# ⑩time.strptime(string[, format])：把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。在这个函数中，format默认为："%a %b %d %H:%M:%S %Y"。
print time.strptime('2017-03-9 09:48:07','%Y-%m-%d %X')#time.struct_time(tm_year=2017, tm_mon=3, tm_mday=9, tm_hour=9, tm_min=48, tm_sec=7, tm_wday=3, tm_yday=68, tm_isdst=-1)

# 10.3.6 random模块
import random
# random模块包含返回随机数的函数，可以用于模拟或者用于任何产生随机输出的程序中。
# ①random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
print random.random()#0.681251479099
# ②getrandbits()以长整型形式返回给定的位数（二进制数）,如果处理的是真正的随机事务（比如加密），这个函数尤为有用
print random.getrandbits(3)
# ③random.uniform的函数原型为：random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。
# 如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。
print random.uniform(10,20)
print random.uniform(20,10)
# ④random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。
# 这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence
print random.choice('asdadas')#s
# ⑤randrange()函数random.randrange的函数原型为：random.randrange([start], stop, [step])，从指定范围内，按指定基数递增的集合中 获取一个随机数。
print random.randrange(10, 100, 2)#结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。
print random.randrange(5)#返回0-5随机整数
# ⑥random.shuffle的函数原型为：random.shuffle(x[, random])，用于将一个列表中的元素原地打乱。没有返回值
lists=[23,345,675,23,65,2]
random.shuffle(lists)
print lists
# ⑦random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
list1=[1,2,3,5,3,4]
list2=random.sample(list1,2)
print list2
#list3=random.sample(list1,8)#不能超出序列最大长度
list3=random.sample(list1,0)
print list3#[]
#练习 自动发牌小程序
values=range(1,11)+'Jack Queen King'.split()
suits='liwei lijie libo congyang'.split()
deck=['%s of %s'%(v,s) for v in values for s in suits]
shuffle(deck)
#while deck:
     #raw_input(deck.pop())

# 10.3.7 shelve模块
# shelve中唯一有趣的函数是open。在调用它的时候(使用文件名作为参数)，它会返回一个Shelf对象，你可以用它来存储内容。只需要把它当做普通的字典(但是键一定要作为字符串)来操作即可，在完成工作(并且将内容存储到磁盘中)之后，调用它的close方法。
#潜在的陷阱
import shelve
s=shelve.open("data.text")
s['x']=['a','b','c']
s['x'].append('d')
print s['x']#结果是['a','b','c']
# 说明：当你在shelf对象中查找元素的时候，这个对象都回根据已经存储的版本进行重新构建吗，当你将元素赋给某个键的时候，它就被存储了，上述列子，
# ①列表['a','b','c']存储在键x下；②获得存储的表示，并且根据它来创建新的列表，而‘d’被天剑到这个副本中，修改的版本还没有保存；③最终，再次获得原始版本--没有‘d’。
# 为了正确地使用shelve模块修改存储的对象，必须将临时变量绑定到获得的副本上，并且在它被修改后重新存储这个副本：
temp=s['x']
temp.append('d')
s['x']=temp
print s['x']
s.close()
# Python 2.4之后的版本还有个解决方法:将。pen函数的writeback参数设为true。如果这样做，所有从shel赎取或者赋值到shel哟数据结构都会保存在内存(缓存)中，并且只有在关闭shelf
# 时候才写回到磁盘中。如果处理的数据不大，并且不想考虑这些问题，那么将writeback设为true(确保在最后关闭了shelf)的方法还是不错的。
#练习 ，数据存储小程序
#① 创建数据存储方法（store_data） ② 创建查询数据的方法（select_data） ③ 输出帮助信息的方法(help) ④接收命令的方法（receive_cmd） ⑤ 主程序方法
def store_data(data_dic):
    pid=raw_input("please enter your id:")
    person={}#创建人员信息字典
    person['name']=raw_input("please enter your name:")
    person['age']=raw_input("please enter your age：")
    person['phone']=raw_input("please enter your phonenumber:")
    print 'Save success!!'
    data_dic[pid]=person
def select_data(data_dic):
    pid=raw_input('enter your id:')
    info=raw_input('what would you like to knom?(name,age,phone)')
    info=info.strip().lower()
    print info.capitalize()+'is :'+data_dic[pid][info]
def help():
    print 'the available commands are:'
    print 'store  : Store information about a person'
    print 'select : Select information about a person'
    print 'quit   : Save change and exit'
    print '?      : Print this message'
def receive_cmd():
    cmd=raw_input('enter command (? for help)')
    cmd=cmd.strip().lower()
    return cmd
def main():
    try:
        data_dic=shelve.open('data.text')
        while True:
            cmd=receive_cmd()
            if cmd=='store':
                store_data(data_dic)
            elif cmd=='select':
                select_data(data_dic)
            elif cmd=='quit':
                data_dic.close()
                return
            else:
                help()
    finally:
        data_dic.close()
#if __name__=='__main__':
    #main()

# 10.3.8 re模块--正则表达式
#1.什么是正则表达式
#① 通配符'.'，点号可以匹配任何字符（除了换行符）。
#例
# '.ython' 可以匹配字符串'python',也可以匹配'jython'、'+ython'、' ython';但是不能匹配'cpython'或者'ython',因为点号只能匹配一个字母，而不是两个或者零个。

#② 对特殊字符进行转义
#例
#'python.org'会匹配'python.org'，但也会匹配'pythonzorg',等，使用转义符：'python\\.org'只能匹配'python.org'

#③ 字符集,使用中括号括起来
#例
#'[pj]ython'可以匹配'python'和'jython'；'[a-z]',能够按照（按字母顺序）匹配a到z的任意一个字符；[a-zA-Z0-9]能够匹配任意一个大小写字母和数字。
#反转字符集：'[^abc]'可以匹配任何除了a、b、c之外的字符

#④ 选择符和子模式 ，管道符号：'|'
# 例
# 只想匹配'python'和'perl',所需的模式可以写成'python|perl',但是有些时候不需要对整个模式使用选择运算符---只是模式的一部分。
# 这时可以使用圆括号括起来需要的部分，或称子模式。可以写成'p(ython|erl)'。（注意术语子模式也适用于单个字符）

#⑤ 可选项和重复子模式：在子模式后面加上问号，它就变成了可选项
#例：
#r'(http:\\)?(www\.)?python\.org',
# 这个模式可以匹配的字符串有：'http:\\www.python.org'、'www.python.org'、'python.org'、'http:\\python.org'
# 上述的例子：①使用原始字符串减少反斜杠的数量；②在使用反斜杠对'.'做了转义；③每个可选子模式都加上了括号；④子模式后面加上问号作为可选项

#⑥(pattern)* 表示允许模式重复0次或多次 ； (pattern)+ 表示允许模式重复1次或多次 ； (pattern){m.n} 表示允许模式重复m至n次。
#例：
#r'W+\.python\.org' 可以匹配'W.python.org'、'WW.python,org'、'WWW.python.org'但不能匹配'.python.org';
#r'W{3,4}\.python\.org' 只能匹配'WWW.python.org'和'WWWW.python.org'

#⑦字符串的开始和结尾：使用 '^'和'$'标记
#例：
#'^ht+p' 这个模式会匹配'http://python.org' 但不会匹配'www.http,org'
#'$ht+p' 这个模式会匹配'www.http' 但不会匹配'www.http,org'等

#2.re模块的内容
# ①函数compile(pattern[,flags])：将正则表达式（以字符串书写的）转换为模式对象，可以实现更有效率的匹配。
# ②函数search(pattern，string[,flags])会在给定的字符串中寻找第一个匹配给定正则表达式的字符串。一旦找到子字符串，函数就会返回MatchObject（值为True）,否则返回None(值为False)
# ③函数match(pattern，string[,flags])会在给定字符串的开头匹配正则表达式，因此 match('p','python')返回True；match('p','www.python.org')返回False
# ④函数split(pattern，string[,flags]，maxsplit=0)会根据模式的匹配项分割字符串并返回一个列表,maxsplit指定列表返回的元素个数，可以不指定
# ⑤函数findall(pattern，string)以列表的形式返回给定模式的所有匹配项。
# ⑦函数sub(pat,rel,string[,maxsplit=0])使用给定的替换内容将匹配模式的子字符串（最左端并且非常重叠的子字符串）替换掉。
# ⑧函数escape(string)对字符串中所有可能被解释为正则运算符的字符进行转义的应用函数。用于代替反斜杠。
#例
import re
pat=compile('l')
str='liwei is a good boy'
if pat.search(str):
    print 'found it'



