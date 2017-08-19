# -*- coding: utf-8 -*-
#11.1 打开文件

# open函数使用给一个文件名作为唯一的强制参数，然后返回一个文件对象。模式（mode）和缓存（buffering）参数都是可选的
# 例：f=open(r'D:\text\somfile.txt')，该路径下不存在该文件会引发异常。
#11.1.1 文件模式
# 如果open函数只带一个文件名参数，那么我们可以获得能读取文件内容的文件对象，因为默认是读模式。
# 'r'           读模式
# 'w'           写模式
# 'a'           追加模式
# 'b'           二进制模式（可添加到其他模式中使用，如：'rb'：表示读取二进制文件）
# '+'           读/写模式（可添加到其他模式中使用）

# 说明：通过在模式参数中使用U参数能够在打开文件时使用通用的换行符支持模式，在这种模式下，所有的换行符/字符串(\r\n,\r或者是\\n)都被转换成\\n，而不用考虑运行的平台。

# 11.1.2 缓冲
# open函数的第3个参数(可选)控制着文件的缓冲。如果参数是0(或者是False)，I/O(输人/输出)就是无缓冲的(所有的读写操作都直接针对硬盘);
# 如果是1(或者是丁rue), I/O就是有缓冲的(意味着Python使用内存来代替硬盘，让程序更快，只有使用flush或者close时才会更新硬盘上的数据—参见11.2.4节)。
# 大于1的数字代表缓冲区的大小(单位是字节)，-1(或者是任何负数)代表使用默认的缓冲区大小。

# 11,2 基本文件方法

# 11.2.1 读和写
#f=open('somefile','w')#创建了一个支持写模式的类文件对象
#f.write('Hello,')#每次调用f.write('string')是，所提供的参数string会追加到文件中已存在部分的后面。
#f.write('Liwei')
#f.close()#关闭文件，将内容写到磁盘
#f=open('somefile','r')
#print f.read(4)#指定读取4个字节
#print f.read()#读取剩下的部分

# 11.2.2 管式输出

# 随机访问
# seek(offset[,whence])这个方法帮当前位置（进行读和写的位置）移动到有offest定义的位置，whence.offset是一个字节（字符）数，whence默认是0，
# 也就是说偏移量是从文件开头开始计算（偏移量必须是非负的）。whence可能被设置为1（相对于当前位置的移动，offset可以是负的）或者2（相对于文件结尾的移动）
#f=open(r'somefile','w')
#f.write('01234567890123456789')
#f.seek(5)#从左至右移动五个位置
#f.write('Hello,Word!')#从第六个位置开始写入，会替换掉等长的字符
#f.close()
#f=open(r'somefile')
#print f.read()
#f=open(r'somefile')
#print f.read(3)
#print f.read(2)
#print f.tell()

# 11.2.3一些操作文件的基本方法
'''
# read(n)
f=open(r'somefile')
print f.read(7)
print f.read(4)
f.close()
with open(r'somefile') as ff:#这种写法无论发生什么情况都会关闭文件
   print ff.read(7)
# read()
f=open(r'somefile')
print f.read()
f.close()
# readline()
f=open(r'somefile')
for i in range(3):
    print str(i)+' : '+f.readline()
f.close()
# write(string)
f=open(r'somefile','w')
f.write('this\nis no\nhaiku')
f.close()
# writelines()
f=open(r'somefile')
lines=f.readlines()
f.close()
lines[1]="isn't a\n"
f=open(r'somefile','w')
f.writelines(lines)
f.close()

'''

# 11.3 对文件内容进行迭代


# read , readline , readlines , xreadlines
def process(string):
    print 'Process:'+string
'''
# 11.3.1 按字节处理
print '按字节处理'
f=open('somefile')
char=f.read(1)#到达文件末尾会返回一个空字符串，这时候就是false了
while char:
    process(char)
    char=f.read(1)#代码重复，需优化
f.close()
print '按字节处理优化版'
f=open('somefile')
char=f.read(1)#到达文件末尾会返回一个空字符串，这时候就是false了
while True:
    char = f.read(1)
    if not char:
        break;
    process(char)
f.close()

# 11.3.2 按行操作
print '按行操作'
f=open('somefile')
while True:
    line=f.readline()
    if not  line:
        break;
    process(line)
f.close()

# 11.3.3 读取所有内容
print '读取所有内容--read()'
#① 使用read()方法，把整个文件当做一个字符串读取
f=open('somefile')
for char in f.read():
     process(char)
f.close()

'''
#② 使用readlines()方法，把整个文件读入一个字符串列表
'''
print '读取所有内容--readlines()'
f=open('somefile')
for line in f.readlines():
     process(line)
f.close()
'''


# 11.3.4 使用 fileinput实现懒惰行迭代
# 说明：在需要对一个很大的文件进行迭代的时候，readlines方法会占用太多内存。这个时候可以使用while循环加readline方法来代替。
# 当然在python中如果能使用for循环，那么他就是首选。下面的列子使用for循环可以使用一个名为懒惰行迭代的方法：说它懒惰行迭代是因为它只是读取实际需要的文件部分
'''
print '使用 fileinput实现懒惰行迭代'
import fileinput
for line in fileinput.input('somefile'):
    process(line)
'''


# 11.3.5 文件迭代器

print '文件迭代器,直接迭代文件对象'
f=open('somefile')
for line in f:
     process(line)
f.close()

for line in open('somefile'):#当没有对文件进行写入的是后可以不执行关闭文件的操作
    process(line)


lines=list(open('somefile'))
print lines
for line in lines:
     process(line)
f.close()

import sys
while True:
    line=sys.stdin.readline().strip()
    if not line:
        break
    process(line)

for line in sys.stdin.readline().strip():#for循环是对每一个字节迭代
    if not line:
        break
    process(line)