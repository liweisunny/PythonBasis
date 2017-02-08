# -*- coding: utf-8 -*-
#抽象：抽象是隐藏多余细节的艺术。定义处理细节的函数可以让程序更抽象。
#函数：编写函数只是给程序需要的部分（也可能是其他程序）提供服务。写在def语句中函数名后面的变量通常叫做函数的形参，而调用函数的时候提供的值是实参，或者称为参数。
#1.使用def定义函数
#例①定义函数隐藏细节实现菲波那切数列
def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])#这里的-2是负数索引，表示列表元素从右边开始第二个元素，-1就是从右边开始第一个元素，也可以理解成倒数第二个元素和倒数一个元素。
    return result;
print callable(fibs)#检测函数是否可用，True表示可用，python3.0以后不在支持callable需要使用表达式hasattr()代替
print fibs(10)

#2.文档化函数：在函数开头写下字符串，它就会作为函数的一部分存储，这称为文档字符串。
#例①
def square(x):
    'Calculates the square of the number x.'
    return x*x
#访问文档字符串：__doc__是函数的属性，属性名中的双下划线表示它是一个特殊属性
print square.__doc__#输出结果：Calculates the square of the number x.

#3.helpe():内建函数help可以得到关于函数，包括它的文档字符串信息。
print help(square)#参数是函数名

######所有的函数都返回了东西，当不需要返回值的时候就会返回None######
#例①
def test1():
    print 'test1()没有设置返回值'
x=test1()
print x#输出结果：None
#例②
def test2():
    print 'test2()有return但没有返回任何值'
    return
    print '这里的return起到的作用就是跳出函数，类似于循环中的break'
x=test2()
print x#输出结果：None

#4.在函数内为参数赋予新值不会改变外部任何变量的值。
#例①
def try_change(name):
    name='liwei'
name='lijie'
try_change(name)
print '调用函数后函数外的name值：%s'%name
#说明：字符串，元组以及数字是不可变的，既无法被修改；
#例②
def change(n):
    n[0]='liwei'
name=['lijie','liwei']
change(name)
print name#结果参数被改变了。
#例③--不适用函数模拟例②的实现过程
name=['lijie','liwei']
n=name#两个变量指向了同一个列表，它们占用的是同一块资源。
print  n is name
print  n==name
n[0]='liwei'
print name
#例④复制例表副本，保留原列表
name=['lijie','liwei']
n=name[:]#使用切片操作，返回一个列表副本，这时候n和name就不是同一个列表了，只是值一样
print  n is name
print  n==name
n[0]='liwei'
print name

#5.使用函数改变数据结构（列表或字典）是一种将程序抽象化的好方法。
#练习：编写一个存储名字并且能够用名字、中间名、姓查找联系人的程序。
#思路：①构造函数初始化一个包含 first  middle  last  数据结构的字典。②构造查询名称是否存在于当前字典中的函数，③定义存储名称的函数
def InitData(dic):
    dic['first']={}
    dic['middle']={}
    dic['last']={}
def searchName(dic ,lable,name):
   return dic[lable].get(name)#使用字典的get方法查询指定key，不存在返回none

def saveNames(dic,full_name):
    names=full_name.split()
    if len(names)==2 :names.insert(1,'')#在names的索引为一的位置插入一个空元素
    lables='first','middle','last';
    for lable ,name in zip(lables,names):
        people=searchName(dic, lable, name)
        if people:
            people.append(full_name)
        else:
            dic[lable][name]=[full_name]
dic_name={}#最终构造成的是一个二维字典，第二个字典的值是列表
InitData(dic_name)#初始化字典。
saveNames(dic_name,'Mr wei li')
saveNames(dic_name,'Mrs jie li')
print dic_name
#说明：在一些其他语言中，重新改变参数，并且是这些改变影响到函数外的变量是很平常的事情，但在python中这是不可能的，python中函数只能修改参数对象本身，但是如果参数不可变，比如数字，那么就没有办法了，唯一的办法就是将其存放到列表或字典中间接改变。

#6.关键字参数和默认值。
#例①
def Hello_Word(greeting,name):
    print '%s,%s'%(greeting,name)
Hello_Word(greeting='hello',name='liwei!')
Hello_Word(name='liwei!',greeting='hello')
#上面两句话说出的结果是一样的，这种使用参数名提供的参数叫做关键字参数，这样就不需要考虑参数的传递顺序了。

#关键字参数的最大作用在于可以在函数中给参数设置默认值,但是设置默认值的参数必须放在没有默认值的参数后面。
def Hello_Word2(greeting='hello',name='liwei'):
    print '%s,%s'%(greeting,name)
Hello_Word2()#不提供任何参数
Hello_Word2(name='lijie')#只提供名称

#7.收集参数
#例①
def print_params(*params):
    print params;
print_params(1)#可以看到结果作为元组打印出来了。
print_params(1,2,'32')#可以看到结果作为元组打印出来了。
#例②
def print_params2(title,*params):
    print '%s is %s'%(title,params);
print_params2('params',1,2,3,'liwei')
#print_params2('params',something='123')#这句话会报错，不能收集关键字参数
#说明：参数前的星号是收集其余位置的参数并将所有值放置在同一个元组中。可以说是将这些值收集起来，然后使用(并且可以和普通参数联合使用，如例②)，但不能收集关键字参数，那怎么解决呢？
#例③使用两个*收集关键字参数
def  print_params3(**params):
    print params;
print_params3(x=1,y=2,z='34')#返回一个字典，而不是元组
#例④
def  print_params4(x,y,z='23',*one,**two):
    print x,y,z
    print one
    print two
print_params4(1,2,3,4,5,foo=1,zoo=2)
#现在学会了收集参数，那么怎么实现多个名字存储呢，优化5-练习
def saveNamess(dic,*full_names):
    for full_name in full_names:
        names=full_name.split()
        if len(names)==2 :names.insert(1,'')#在names的索引为一的位置插入一个空元素
        lables='first','middle','last';
        for lable ,name in zip(lables,names):
            people=searchName(dic, lable, name)
            if people:
                people.append(full_name)
            else:
                dic[lable][name]=[full_name]
dic_name={}#最终构造成的是一个二维字典，第二个字典的值是列表
InitData(dic_name)#初始化字典。
saveNamess(dic_name,'Mr wei li','Mrs jie li','Mrs congyang qu','Mr bo li')
print dic_name

#8.参数收集的逆过程
#例①
def add(x,y):
    return x+y
params=(1,2)
#add(params)#报错
print add(*params)#分割参数，得到结果3
#例②
def helloword(greeting,name):
    print '%s,%s'%(greeting,name)
name={'greeting':'hello','name':'liwei'}
helloword(**name)

#9.作用域（命名空间）参考书籍103
#例①
x=1#这个简单的赋值语句，名称x引用到值1，就像字典一样，键引用值，当然变量和所对应的值用的是一个’不可见‘字典。这个’不可见字典‘就是作用域或命名空间。这里是全局作用域
scope=vars()#内建函数vars()返回当前作用域下的不可见字典。
print  scope['x']#输出结果为：1
#例②
def foo():
    x=42
x=1
foo()
print x#结果为：1，因为每个函数调用都会创建一个新的作用域，函数内的变量被称为局部变量，两个x一个是局部变量，一个是全局变量。
#例③--函数内部访问全局变量
def comb(x):
    print x+y
y=2
comb(1)
#如果局部变量或者参数的名字和想要访问的全局变量同名，那么全局变量就会被屏蔽掉。
#例③
def adds(x):
    y=2
    print x+y
y=1
adds(22)#结果就是24而不是23
#例④--强制访问全局变量
def adds(x):
    y=2
    print x+globals()['y']#强制访问全局变量
y=1
adds(22)#结果就是23
#如果在函数内部将值赋予一个变量，那么它会变成局部变量，除非告诉python将其声明为全局变量
#例⑤
x=1
def gloab():
    x=2
    print x+1
gloab()#3
#例⑥--尽量不要使用
def gloab2():
    global x#使用global声明表示为全局变量
    print x+1
gloab2()#2
#10.闭包，参考书籍105

#11.递归

#12.二分查找