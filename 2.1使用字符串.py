# -*- coding: utf-8 -*-
'''
#基本字符串操作，索引、分片、乘法、判断成员资格、求长度、取最大最小值等，但请记住字符串是不可变的，so 通过分片赋值都是不合法的。
x='liwei is a good boy'
#x[1:3]='co' 会出错的
print x
'''

#字符串格式化：精简版
'''
#实现方式：使用%，在%左侧放置一个字符串（需要被格式化的字符串），右侧放置希望被格式化成的值，可以使用一个值，如一个字符串或者一个数字；（也可以使用多个值的元组或者下章将会讨论到的字典，前提是需要格式化多个值），一般情况下使用元组
format="hello %s . My Name is %s"
words=('Word','LiWei')
print format%words
#说明：格式化操作符的右操作数可以是任意类型，如果右操作数是元组的话，则其中的每一个元素都会被单独格式化，每个值都需要一个对应的转换说明符，并且元组作为转换表达式的一部分存在时，必须使用圆括号括起来。
# 转换说明符：它们标记了需要插入转换值的位置。s表示值会被格式化为字符串--如果不是字符串，则会用str函数将其转换为字符串。
#如果使用列表或者其他序列代替元组，那么序列会被解释为一个值，只有元组和字典可以格式化一个以上的值。
format="hello %s . My Name is %s"
words=['Word','LiWei']
#print format%words 出错。

#格式化实数（浮点数），可以使用f说明转换说明符的类型，同时提供所需要的精度：一个句点在加上希望保留的小数位数，因为格式化转换说明符总是以表示类型的字符结束，so 精度应该放在类型字符的前面
format="Hello,My Height is %.2f m"
vales=(1.765)
print format%vales

format="Pi with three decimal:%.3f"
from math import pi
print format%pi

#模板字符串：string模块提供的另外一种格式化字符的方式。
#substitute这个模板方法会用床底进来的关键字参数foo替换字符串中的$foo,并返回替换后的值。
from string import Template #导入模板
s=Template('$x. glorious $x!')#包装字符串
print s.substitute(x='slurm')#调用模板方法格式换字符串

#如果替换字段是单词的一部分，那么参数名就必须用括号括起来，从而准确指明结尾：
s=Template("It's ${x}tastic!")
print s.substitute(x='slurm')

#可以使用$$插入美元符号
s=Template("Make $$ selling $x!")
print s.substitute(x='slurm')

#除了关键字参数外，还可以使用字典变量提供值/名称对
s=Template("A $thing must never $action.")
d={}
d['thing']='gentleman'
d['action']='show his socks'
print s.substitute(d)
#说明safe_substitute相比substitute不会因为缺少值或者不正确使用$字符而出错
'''

#字符串格式化：完整版
#基本的转换说明符：
'''
①%字符串：标记转换说明符的开始
②转换标志（可选）：-表示左对齐、+表示在转换值之前加上正负号、""(空白字符)表示正数之前保留空格、0表示转换值若位数不够则用0填充。
③最小字段宽度（可选）：转换后的字符串应该具有改制指定的宽度。如果是*，则宽度会从元组中读取出。
④点（.）后面跟精度值（可选）：如果转化的是实数，精度值就表示出现在小数点后的位数。如果转换的是字符串，那么该数字表示最大字段宽度。如果是*，那么精度将会从元组中读出。
⑤转换类型
s，获取传入对象的__str__方法的返回值，并将其格式化到指定位置
r，获取传入对象的__repr__方法的返回值，并将其格式化到指定位置
c，整数：将数字转换成其unicode对应的值，10进制范围为 0 <= i <= 1114111（py27则只支持0-255）；字符：将字符添加到指定位置
o，将整数转换成 八 进制表示，并将其格式化到指定位置
x，将整数转换成十六进制表示，并将其格式化到指定位置
d，将整数、浮点数转换成 十 进制表示，并将其格式化到指定位置
i，同上
e，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
E，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（大写E）
f， 将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
F，同上
g，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是e；）
G，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是E；）

#基本练习
print "my age is %d" % 42
print 'Using str : %s' % 42L
print 'Using repr : %r' % 42L
from  math import pi
print 'Pi is %f......' % pi
print 'very inexact estimate of pi:%i' % pi
'''
'''
#字段的宽度和精度
# 转换说明符可以包括字段宽度和精度。字段宽度是转换后的值所保留的最小字符个数，精度则是结果中应该包含的小数位数（对于数字），或者是转换后的值所能包含的最大字符个数（对于字符串）
#宽度和精度都是整数，首先是字段宽度，然后是精度，通过点号（.）分隔，虽然都是可选参数，但是如果只给出精度那么必须包含点号。
print '%10f' % pi #字段宽度10
print '%10.2f' %  pi #字段宽度10 精度2
print '%.2f' % pi  #字段精度2
#可以使用*号作为字段的宽度或者精度，此时熟知会从元组中获取
print '%.*f' %(2,pi) #精度2
print '%*s' %(5,"liwei")
print '%*.*s' %(2,3,"liwei")
#符号、对齐、和用0填充
print '%010.2f'% pi
print '%-10.2f' % pi#左对齐
print ('% 5d' % 10)+'\n'+('% 5d' % -10)#在正数前加上空格，这可用来对齐正负数。
print ('%+5d' % 10)+'\n'+('%+5d' % -10)#无论是正负数都标记出符号
'''
#字符串方法
'''
#find方法，在一个较长的字符串中查找字串，返回字串所在位置的最左端索引，如果没有找到则返回-1，还可以指定查找范围。
strs='liwei is g good boy!!!'
print strs.find('is')#6
print strs.find('lir')#-1
print strs.find('is',3)#指定查找的起点是索引为3的位置，包括3，，，6
print strs.find('is',3,7)#指定查找的起点和终点，但不包括终点，，，-1
'''


#join方法是非常重要的字符串方法，它是split方法的逆方法，用来连接序列中的元素。
strs=[1,2,3,4,5]
#print '+'.join(strs) 出错，因为join徐亚连接的序列元素必须都是字符串
strs=['1','2','3','4']
print '+'.join(strs)#1+2+3+4
strs='liwei','lijie'
print '--fuck-->'.join(strs)

#lower返回字符串的小写字母版
strs='LIWEi is A Good Boy'
print strs.lower();

#replace方法返回某字符串的所有匹配项均被替换后得到的字符串
strs='liwei Is is nice boy'
print strs.replace('is','very')

#split方法：将字符串分割成序列
strs='1+2+3+4';
print strs.split('+')
strs='1,2,3.4/5'
print strs.split(',')
strs='1 2   3,4'
print strs.split()#不指定分隔符会默认把所有的空格作为分隔符（空格，制表，换行）

#strip方法：去除两侧的空格，不包含内部的
strs='    123 3323  34      '
print strs.strip()
strs='!*12321!*221!*1231!*'
print strs.strip('!*')#去除指定的字符，但只是去除两侧的。

#translate方法和replace类似，可以替换字符串中的某些部分，但是和前者不同的是，translate方法只处理单个字符。它的优势在于可以同时进行多个替换，意思就是替换多种字符，有些时候会比replace效率高的多。

#练习，将纯正的英文文本转换为带有德国口音的版本，那么需要将字符c替换成k,s替换成z.
#步骤 ①获取转换表，转换表中是以某字符替换某字符的对应关系。使用string模块的maketrans函数就行。
from string import maketrans
table=maketrans('cs','kz')
strs='this is an incredible test'
print strs.translate(table)
print strs.translate(table,' ')#第二个参数是可选的，用来指定要删除的字符








