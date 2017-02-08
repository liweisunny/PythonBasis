# -*- coding: utf-8 -*-

#使用逗号输出
print "age",22
print 1,2,3
name='liwei'
age=22
print name+"'s age ", age

#赋值---序列解包：或递归解包---将多个值的序列解开，然后放到变量的序列中。当函数或者方法返回元组的时候这个特性很有用。
x,y,z=1,2,3#这个操作执行的过程其实就是下面这段代码
print x,y,z

values=1,2,3
print values
x,y,z=values
print x,y,z
#说明：所解包的序列元素数量必须和放置在赋值符号=左边的变量数量完全一致，否则Python会在赋值是引发异常。

#赋值---链式赋值
x=y=1
print x,y

#赋值---增量赋值
x=2
x+=1
x*=2
print x
#对于其他的数据类型也和适用
x='liwei'
x+='lijie'
x*=2
print x



