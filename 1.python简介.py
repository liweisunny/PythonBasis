# -*- coding: utf-8 -*-
'''
#输出函数
print ("hellow weord !");
print (123);
'''

'''
#赋值函数，用户输入任意值 python3.0以后input和raw_input合体了， python3.0中input接受的是字符串
x=input("x:");
y=input("y:");
print (x*y);

name=input("what is your name?")
#print("your name is "+name)#存在问题，因为input会假设用户输入的是合法的python表达式，如果以字符串输入名字是不会报错的，然而要求用户带着引号输入名字有点过分，
#这时就需要用到raw_input()函数，它会把所有的输入当做原始数据，然后将其放入字符串中。python3.0以后input和raw_input合体了， python3.0中input接收的是字符串。
name=raw_input("what is your name?")
print("your name is "+name)
'''

'''

'''
#内建函数

#幂函数 pow()
x=pow(2,3);
print (x);

#绝对值函数 abs()
y=abs(-10)
print(y)

#四舍五入函数
z=round(1.0/2.0)#？？？存在问题，小数位置为5的时候舍掉了
print(z)
'''

'''
#模块：可以想象成导入到python以增强其功能的扩展。需要使用特殊的命令import来导入模块。
import math  #导入模块
#写法1
x=math.floor(32.9) # 转换为小于他的最大整数的函数，使用方式--模块.函数
print(x)
y=math.ceil(32.9) # 转换为大于他的最小整数的函数，使用方式--模块.函数
print(y)
z=math.sqrt(4) # 求平方根的函数 ，使用方式--模块.函数
print(z)
# 写法2
foo=math.sqrt # 将函数赋值给一个变量
print(foo(4))
# 写法3
from math import sqrt #一旦使用了这种写法，就没法使用普通的sqrt函数了（cmath.sqrt(-1)会出错），会造成命名冲突，所以不建议使用这种方式
print (sqrt(4));
#print(sqrt(-1))# 报错

import cmath
print (cmath.sqrt(-1))# 负数求平方根值是一个虚数
'''

'''
#转义符 \
print("hello\" liwei")

#字符串拼接
print("hello""liwei")#特殊写法
print("hello "+"liwei")#正规写法
x="hello "
y="liwei"
print(x+y)

#值被转换成字符串的两种机制，str()函数和repr()函数
#str()函数会把值转换为合理形式的字符串，而repr()函数会创建一个字符串，它以合法的python表达式的形式来表示值
#简单来说str、repr函数是将python值转换为字符串的两种方法，函数str让字符串更易于阅读，而repr则把结果字符串转换为合法的python表达式。
print (repr("hello. word!"));
print (str("hello. word!"));

temp=42;
print("thw number is "+ repr(temp))
print("thw number is "+ str(temp))

#长字符串
print('''liwei
shi ge da
hao ren''')#也可以使用三个双引号

#原始字符串，以r开头，这样反斜杠就失去了转义的功能
print(r"C:\user\liwei")
print(r"C:\user\liwei""\\")












