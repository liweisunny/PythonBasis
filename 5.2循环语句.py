# -*- coding: utf-8 -*-
'''
#循环 --- while:用来在任何条件为真的情况下重复执行一个代码块
#列①
x=1
while x<=100:
    print x
    x=x+1
#列②
name=""
print not name.strip()
while not name.strip():
    name=raw_input('Please enter your name:')
    if not name.strip():
        print " enter error!!!:"
    else :
        print "hellow, %s!"%name
#列③ 优化 列①
for num in range(1,101):
    print num
'''
'''
#循环 --- for循环--迭代序列
#列①
words=['liwei','lijie','libo','qucongyang']
for word in words:
    print word;
#列②
numbers=[1,2,3,4,5,7,8]
for num in numbers:
    print num;
#range()函数：工作方式类似于分片，用于提供某一范围内的数字，报包含下限，不包含上限，如果希望下限为0，就可以只提供上线。

#s说明：如果能使用for循环尽量不要使用while循环
#列③--循环遍历字典元素
dic={'x':1,'y':2,'z':3}
for key in dic:
    print "%s's value is %s"%(key,dic[key])
#列④--for循环汇总使用序列解包
for key,value in dic.iteritems():
    print key,value;
#说明：迭代的时候字典中的键值都能保证被处理，但是迭代的顺序是不确定的，如果顺序很重要，可以将键值分别保存到列表中迭代。
'''
'''
#并行迭代
#列① --- 同时打印姓名和对应的年龄
names=['liwei','lijie','libo','congyang']
ages=[20,21,22,23]
for i in range(len(names)):
    print '%s age is %s'%(names[i],ages[i])
#列②---使用内建的zip函数进行并行迭代，它可以把两个序列压缩在一起然后返回一个元组列表
print zip(names,ages)
for name ,age in zip(names,ages):#实现原理序列解包
    print '%s age is %s' % (name, age)
#列③zip函数可以作用于任意多的序列，并且可以处理不等长的序列，当最短序列用完的时候就会停止
print zip(range(5),xrange(100))
#说明：！！！这里不推荐用range替换xrange，range函数一次创建整个序列，会计算所有的数字，这要花费很长时间，而xrange一次只创建一个数，这里它只会计算前5个数字。
'''

'''
#按索引迭代--有些时候想要迭代访问序列中的对象的同时还要获取当前对象的索引值
#列①--在一个字符串列表中替换所有包含'xxx'的字符串为'lili'
strings=['liwei','lijie','wangbo']
for string in strings:
    if 'li' in string:
        index=strings.index(string)#搜索给定的字符串，获取当前满足条件的字符串的索引值，用于后续替换，这种方式显然可以完成功能需求，但并不高效。
        strings[index]='lili'
print strings
#列②---列①的升级版
strings=['liwei','lijie','wangbo']
index=0;#f方法有些笨拙，不过可以接受
for string in strings:
    if 'li' in string:
        strings[index]='lili'
        index+=1
print strings
#列③--使用内建函数enumerate该函数可以在提供索引的地方迭代索引-值对。
strings=['liwei','lijie','wangbo']
for index,string in enumerate(strings):
    if 'li' in string:
        strings[index]='lili'
print strings
'''
'''
#翻转和排序迭代：reversed和sorted,它们同列表的reverse和sort方法类似，但作用于任何序列或者可迭代对象上，不是原地修改对象而是返回翻转或排序后的版本。
print sorted([4,2,3,1,5])
print sorted('hello,world!')
print list(reversed([1,3,2,4,1,5]))
print list(reversed('hello,word!'))
print ''.join(list(reversed('hello,word!')))
#说明：sorted方法返回列表，reversed方法返回可迭代对象
'''

'''
#跳出循环
#break:跳出循环，
#列① 求100以内的最大平方数
from math import sqrt
for num in range(99,0,-1):
     root=sqrt(num)
     if root==int(root):
         print num;
         break;#跳出循环

#continue:跳出本次循环，不是很常用，要习惯使用break,因为在while True语句中会经常用到它
'''

'''
#While True/break习语
#列①
str='liwei'#在这里，在进入循环之前，我们个str赋了一个哑值（未使用的值），使用哑值就是工作没有尽善尽美的标志。
while  str:
    str=raw_input("please enter you name :")
    print 'your name is %s'%str

#列②

str = raw_input("please enter you name :")#哑值没了，但是代码重用
while  str:
    print 'your name is %s'%str
    str=raw_input("please enter you name :")

#列③
while True:#While True/break
    str=raw_input("please enter you name :")
    if not str:
        break;
    print 'your name is %s' % str
'''
#循环中else语句
'''
from math import sqrt
for num in range(99,81,-1):
     root=sqrt(num)
     if root==int(root):
         print num;
         break;#跳出循环
else:#仅在没有调用break之前执行，意思是执行一次
    print 'not found!!'
'''
#列表推倒式--轻量级循环
#列表推倒式是利用其它列表创建新列表的一种方法，它的工作方式类似于for循环，也很简单：
#列①
lis=[]
for x in range(10):
    lis.append(x*x)
print lis;
#列①的简化版
print [x*x for x in range(10)]#打印出0到9所有整数的平方
#列②
lis=[]
for x in range(10):
    if x%3==0:
        lis.append(x*x)
print lis
#列②的简化版
print [x*x for x in range(10) if x%3==0]#打印出0到9之间能被3整除的所有整数的平方
#列③
lis=[]
for x in range(5):
    for y in range(5):
        if x%3==0:
            lis.append((x,y))
print lis
#列③的简化版
print [(x,y) for x in range(5) for y in range(5) if x%3==0 ]

#列④
girls=['liwei','alice','xiexie']
boys=['xiele','lijie','abc']
result=[b+"+"+g for b in boys for g in girls if b[0]==g[0]]#将首字母相同的关联到一起。这个方法不是很高效，因为它会检查每个可能的配对。
print result
#列④--优化 先将女孩集合的首字母和对应的值存放到字典中，注意值是一个列表，在根据男孩的首字母去遍历字典中对应的列表
dic={}
for x in girls:
    dic.setdefault(x[0],[]).append(x)#为字典添加键，并设置默认值为空列表，setdefault返回当前键的值，然后在向列表中增加至
result=[b+"+"+g for b in boys for g in dic[b[0]]]
print result













