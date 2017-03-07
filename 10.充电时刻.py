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

# 10.1.4 包
# 为了组织好模块，你可以将它们分组为包(package)。包基本上就是另外一类模块，有趣的地方就是它们能包含其他模块。
# 当模块存储在文件中时(扩展名.Py)，包就是模块所在的目录。为了让Python将其作为包对待，它必须包含一个命名为__init__.py的文件(模块)。如果将它作为
# 普通模块导入的话，文件的内容就是包的内容。比如有个名为 Constants包，文件Constants/__init__.py包括语句PI=3.14，那么你可以像下面这么做:
import  Constants
print Constants.Pi

# 10.1.5 探究模块
#例①  导入copy模块，以此为例介绍
import copy

#dir函数： 查看模块包含的内容可以使用dir函数，它会将对象(以及模块的所有函数、类、变量等)的所有特性列出。如果想要打印出dir(copy)的内容，你会看到一长串名字(试试看)。
# 一些名字以下划线开始一一暗示(约定俗成)它们并不是为在模块外部使用而准备的。所以让我们用列表推导式过滤掉它们:
print [n for n in dir(copy) if not n.startswith('_')]

#__all__变量：这个变量包含一个列表，该列表与我之前通过列表推导式创建的列表很类似—除了这个列表在模块本身中被设置。我们来看看它都包含哪些内容:

print copy.__all__

# 说明：这个变量在copy模块内部被设置：__all__=['Error', 'copy', 'deepcopy']；它定义了模块的公有接口。更准确的说，它告诉解释器：从模块导入所有名字代表什么含义，
# 因此，如果如果使用如下代码：
from copy import  *
# 那么你只能使用__all__变量中的三个函数，如果你要导入其它函数（如：PyStringMap），你就得显示地实现，
# 或者导入copy然后使用copy.PyStringMap,或者使用 from copy import PyStringMap。
# 在编写模块的时候，像设置__all__这样的技术是相当有用的。因为模块中可能会有一大堆其他程序不需要或不想要的变量、函数和类，__all__会“客气地”将它们过滤了出去。
# 如果没有设置__all__，用import* 语句默认将会输出模块中所有不以下划线开头的全局名称。
