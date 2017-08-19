# -*- coding: utf-8 -*-
#15.1 屏幕抓取:下载网页源代码分心结构提取数据

#例① 简单的屏幕抓取
from urllib import urlopen
import  re
p=re.compile('<h3><a href="(.*?)">(.*?)</a>')
text=open('Test.html').read()
for url,name in p.findall(text):
    print '%s (%s)'%(name,url)

#说明：上述方法存在三个缺点：
# ①正则表达式并不是完全可读的，对于更复杂的HTML代码和查询来说，表达式会变得论七八糟并且不可维护。
# ②程序对于CDATA部分和字符实体（比如&amp:）之类的HTML特性是无法处理的。如果碰到了这类特性，程序很有可能会失败。
# ③正则表达式被HTML源代码约束，而不是取决于更抽象的结构，这就意味着网页结构中很小的改变就会导致程序中断。

#15.1.1 TIdy和XHML
# XHML是HTML最新的方言，是XML的一种形式
# Tindy：python库，是用来修复不规范且随意的HTML的工具，它能以相当智能的方法修复一般的错误,返回XHTML。便于解析工作的进行
#例② 校正错误的HTML代码
'''
from subprocess import Popen,PIPE
text=open('Error.html').read()
tidy=Popen('tidy',stdin=PIPE,stdout=PIPE,stderr=PIPE)
tidy.stdin.write(text)
tidy.stdin.close()
print tidy.stdout.read()
'''


# XHTML相对于HTML的好处在于：①显示关闭所有元素要求严格，有明确的开始标记和结束标记，便于解析；②XHTML是XML的一种，所以对它可以使用XML工具，例如：XPATH
# 解析这类从Tidy中获得的表现良好的XHTML的方法是使用标准库模块（和类）HTMLParser

#HTMLParser:使用方式就是继承它，然后对它的handle_starttage或handle_data等事件处理方法进行覆盖。

#例③ 使用HTMLParser模块的屏幕抓取（例①的优化版）
from urllib import urlopen
from  HTMLParser import  HTMLParser
class MyParser(HTMLParser):
    in_h3=False
    in_link=False
    def handle_starttag(self, tag, attrs):#找到开始标签的时候调用
        attrs=dict(attrs)
        if tag=='h3':
            self.in_h3=True
        if tag=='a' and 'href' in attrs:
            self.in_link=True
            self.chunks=[]
            self.url=attrs['href']
    def handle_data(self, data):#处理文本数据的时候调用
        if self.in_h3 and self.in_link:
            self.chunks.append(data)
    def handle_endtag(self, tag):#找到结束标签的时候调用
        if tag=='h3':
            self.in_h3=False
        if tag=='a':
            if self.in_h3 and self.in_link:
                print '%s (%s)'%(''.join(self.chunks),self.url)
            self.in_link=False
text=open('Test.html').read()
parser=MyParser()
parser.feed(text)
parser.close()
# 上述例子并没有使用Tidy因为网页中的HTML已经足够规范，这个版本的代码相对于例①来说更能应对html元素的变化，但代码过长，理解诶起来也比较困难，接下来让我们看另一种方法。

#Beautiful Soup：是个小模块用来解析和检查经常在网上看到的乱七八糟而且不规范的HTML
#例④ 使用Beautiful Soup的屏幕抓取程序
from urllib import urlopen
import bs4
from bs4 import BeautifulSoup
text=open('Test.html').read()
soup=BeautifulSoup(text)#实例化BeautifulSoup类
jobs=set()#创建一个集合
for header in soup('h3'):#soup('h3')表示获得所有h3元素
    links=header('a')
    if not links:
        continue
    link=links[0]
    jobs.add('%s (%s)'%(link.string,link['href']))#link.string表示链接中的文本，link['href']表示链接中href属性的值
print '\n'.join(sorted(jobs,key=lambda s:s.lower()))#集合指定排序输出

#15.2 使用CGI创建动态网页
#CGI是网络服务器可以将查询（一般是通过Web表单提交）传递给专门的程序，并在网页中显示结果的的标准机制。



