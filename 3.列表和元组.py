# -*- coding: utf-8 -*-
#python中包含6种内奸序列，最常用的两种类型是列表和元组，其他的内建序列类型有字符串，Unicode字符串、buffer对象和xrange对象。

#列表--可变序列
'''
x=["liwei",22]#列表x

y=["lijie",22]#列表y

database=[x,y]#列表database

print(database)
'''
#列表--索引
'''
print (database[0])#索引从0开始，指向第一个元素
print ([x,y][0])#索引从0开始，指向第一个元素
print (database[-1])#使用负数索引时，python 会从右边，也就是最后一个元素开始计数，最后一个元素的编号是-1.
z="Hello"#一个字符串序列
print (z[0])
print ("Hello"[0])#直接使用字符串的字面值
print (z[-2])
#练习，获取用户输入的年份的第四位数字
year=raw_input("year:")[3]
print ("fourth:"+year)
'''
#列表--分片
'''
#与使用索引访问元素类似，可以使用分片来访问一定范围内的元素，分片通过以冒号分开的两个索引实现
tag='liwei is good'
print (tag[2:5])#wei
number=[1,2,3,4,5,6,7,8,9,10]
print (number[3:8])
#说明：分片操作对截取序列的一部分十分有用，第一个索引是要提取的第一个元素的编号，最后一个索引是分片后剩余部分的第一个元素的编号，简而言之第一个索引元素包含在分片内，第二个则不包含在分片内。
print (number[7:10])#索引10指向的是第11个元素，但是这个元素并不存在，却是在最后一个元素之后，so 这样写也是可行的。
print (number[-3:0])#结果为空，分片中最分左边的索引比他右边的索引晚出现在序列中，结果就是一个空序列。
print (number[-3:])#如果分片所得部分包括序列结尾的元素，那么，只需要置空最后一个索引即可。
#说明：为了让分片部分包含列表的最后一个元素，必须提供最后一个元素的下一个元素所对应的索引作为边界。
print (number[:3])#获取前三位
print (number[:])#复制整个索引
#分片---步长
print (number[0:10:1])#最后一位是步长
print (number[0:10:2])#[1, 3, 5, 7, 9]
print (number[::4])#取出每4个元素的第一位
#说明：补偿不能为0(那不会执行)，但不常可以使负数，此时分片从右到左取元素。
print(number[8:3:-1])#[9, 8, 7, 6, 5]
print (number[10:0:-2])#[10, 8, 6, 4, 2]
print (number[0:10:-2])#[]
print (number[::-2])
print (number[::2])
#说明：当使用一个负数作为步长的时候，必须让开始点大于结束点,对于一个正数步长，python会从序列的头部开始向右提取元素，直到最后一个元素，
# 而对于一个负数的步长，则是从序列的尾部开始向左提取元素，直到最后一个元素
'''
'''
#序列--相加
x=[1,2,3]
y=[4,5,6]
print (x+y)
z="hello "
m="word"
print (z+m)
#print (x+z)#出错
#说明：列表和字符串是无法相加在一起的，尽管他们都是序列，简单来说，两种相同类型的序列才能相加在 一起

#序列--乘法
x='python '
print (x*5)
y=[2,3,4]
print (y*3)
#初始化一个长度为10的空列表，并且不包含任何有效值
x=[None]
print (x*10)
#练习
sentence=raw_input("sentence:")
screen_width=80
text_width=len(sentence)
box_width=text_width+6
left_margin=(screen_width-box_width)//2
print
print ('  ' * left_margin + '+'   +  '_' * (box_width-2) + '+')
print ('  ' * left_margin + '|  ' +  ' ' *  text_width   + '  |')
print ('  ' * left_margin + '|  ' +         sentence     + '  |')
print ('  ' * left_margin + '|  ' +  ' ' *  text_width   + '  |')
print ('  ' * left_margin + '+'    +  '_' *  (box_width-2) +  '+')
print
'''
'''
#序列--成员资格
# in 运算符--返回bool值
x='liwei'
print ('w' in x)
y=[1,2,3,4]
print (1 in y)
user=['liwei','lijie']
n=raw_input('enter your name:')
print (n in user)

subject='$$$ Get rich now!!!'
print ('$$$'in subject)
#说明：最初的三个例子都是使用了成员资格测试来检查的。最后一个检查字符串是在python2.3以后支持的，不属于成员资格检测，因为字符串的成员或者元素是他的某个字符，而不是多个字符组成的字符串。

'''
'''
#序列-长度、最大值、最小值函数
#内建函数 len、max、min，len函数返回序列中包含元素的数量，min函数和max函数则分别返回序列中最大和最小元素
numbers=[10,40,30]
print (len(numbers))#3
print (min(numbers))#10
print (max(numbers))#40
print (max(2,3,5))#5
print (min(2,3,5))#2
#说明：max函数和min函数的参数可以不是一个序列，还可以以多个数字直接作为参数。

#序列--list函数
x=list('hello')#将字符串转换成列表
print (x)
#说明：list函数适用于所有类型，而不只是字符串。
'''

'''
#改变列表---元素赋值
x=[1,1,1]
x[0]=2
#x[4]=3#不能为不存在的位置赋值
print (x)

#删除元素
name=['liwei','lijie','libo','qucongyang']
del name[2]#s删掉索引为2的元素
print (name)

#分片赋值
name=list('liwei')
print (name)
name[2:]=list('jie')
print (name)
numbers=[1,5]
numbers[1:1]=[2,3,4]#分片赋值语句可以在不替换任何原有元素的情况下插入新元素
print (numbers)
numbers=[1,2,3,4,5]
numbers[1:4]=[]
print (numbers)#结果相当于del numbeis[1:4]
'''
#列表中的方法
'''
#append方法用于在列表末尾追加新对象,没有返回值
lst=[1,2,4]
lst.append(3)
print (lst)
#说明：append方法是修改原有列表，而不是返回一个新的列表

#count方法统计某个元素在列表中出现的次数
lst=['liwei','lijie','liwei']
print (lst.count('liwei'))#2
lst=[[1,2],[2,1],[1,2]]
print lst.count(1)#0
print lst.count([1,2])#2

#extend方法可以在列表的末尾一次性追加另外一个血猎中的多个值。换句话说，可以用新列表扩展原有列表,他没有返回值。
lst1=[1,2,3]
lst2=[4,5,6]
lst1.extend(lst2)#这个操作看起来很像链接操作，两者的主要区别在于extend是修改了原有的列表，而原始的链接操作则是返回了一个新列表
print lst1
#原始的连接操作 相对于extend方法效率会很低
a=[1,2,3]
b=[4.5,6]
a+b
print a

#index方法用于从列表中找出某个值第一个匹配结果,返回索引值
lst=['liwei','lijie','liwei','123']
print lst.index('liwei')
#print lst.index('1')找不到会报错

#insert方法用于将对象插入到列表中
numbers=[1,2,3,5,6]
numbers.insert(3,"four")#在索引位置为3的地方插入
print numbers

#pop方法会移除列表中的一个元素（默认是最后一个）。并且返回改 元素的值
numbers=[1,2,3,4]
print numbers.pop()
print numbers
print numbers.pop(1)
print numbers
#说明：pop方法是唯一一个既能修改列表又能返回元素值（none除外）的列表方法
numbers=[1,2,3,4]
numbers.append(numbers.pop())#出栈和入栈的实现，后进先出
print numbers
numbers.insert(numbers.pop(0),numbers.pop(0))#队列 先进先出
print numbers

#remove方法移除列表中某个值的第一个匹配项
x=['liwei','lijie','123']
x.remove('liwei')
print x
#x.remove('321')不存在会报错
#说明：remove是一个没有返回值的原位置改变方法，它修改了列表却没有返回值，这与pop方法相反。

#reverse方法将列表中的元素反向存放但不返回值。
x=[1,2,3]
x.reverse()
print x
#sort方法用于在原始位置队列表进行排序。在原位置排序意味着改变原来的列表，从而让其中的元素能按一定的顺序排列，而不是简单的返回一个已排序的列表副本

x=[2,1,3]
y=x[:] #这种方式不等于y=x,这是获取已排序列表副本的方法，使用分片赋值或者使用sorted函数
x.sort()
print x
print y

x=[1,3,4,2]
y=sorted(x)
print x
print y
#sorted函数可以用于任何序列，却总是返回一个列表
print sorted("liwei")#['e', 'i', 'i', 'l', 'w']

x=[1,3,2,4]
x.sort()
y=x#这种赋值方式x和y都指向了同一个列表,获取不到源列表
print x
print y
'''
#高级排序
number=[1,4,7,2,8,3]
number.sort(cmp)
print number

number=['liwei','lijiejie','li']
number.sort(key=len)#根据字符串长度排序
print number

number=[1.5,2,6]
number.sort(reverse=True)#True表示将列表反转,False得到的还是原来的列表
print number


#元组---不可变序列
1,2,3
(1,2,3)
#上面两种都是元组，不过大部分时候都用括号包裹起来
()#空元组
(2,)#包含一个值的元组，必须加逗号，即使只有一个值
x=tuple([1,3,4])#tuple函数以一个序列作为参数并把它转换为元组，如果参数就是元组，会被原样返回
print x
y=tuple("liweei")
print y
z=tuple((1,4,3))
print z;
x=[1,3,2]
print x[1]#索引查询
print x[0:2]#分片查询
#说明：元组存在的意义，即：元组的不可替代性：元组可以在映射（和集合的成员中当做键使用，而列表则不行）；元组作为很多内建函数和方法的返回值存在，也就是说你必须对元组进行处理。


#小结：




