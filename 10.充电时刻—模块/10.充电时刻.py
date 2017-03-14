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
os.system(r'C:\"Program Files (x86)"\"Google\Chrome"\"Application"\chrome.exe')#注意每个目录下的双引号
# 注意，我很仔细地将Program Files和Google\Chrome以及Application放入引号中，不然DOS(它负责处理这个命令)就会在空格处停下来(对于在PYTHONPATH中设定的目录来说，这点也同样重要)。
# 同时，注意必须使用反斜线，因为DOS会被正斜线弄糊涂。如果运行程序，你会注意到浏览器会试图打开叫做Files"\…的网站一也就是在空格后面的命令部分。
# 另一方面，如果试图在IDLE中运行该代码，你会看到DOS窗口出现了，但是没有启动浏览器并没有出现，除非关闭DOS窗口。总之，使用以上代码并不是完美的解决方法。
# 另外一个可以更好地解决问题的函数是Windows特有的函数：os.startfile:
os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
# 可以看到，os.startfile接受一般路径，就算包含空格也没问题(也就是不用像在os.system例子中那样将Program Fiels放在引号中)。
# 注意，在Windows中，由os.system(或者os.startfile)启动了外部程序之后，Python程序仍然会继续运行，而在UNIX中，程序则会中止，等待os.system命令完成。
#更好的解决方案
import webbrowser #该模块的open函数可以自动启动web浏览器并打开指定的url
webbrowser.open('http:\\www.python.org')#如果url=""会打开当前项目路径

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


