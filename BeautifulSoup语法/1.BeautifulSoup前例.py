# -*- coding: utf-8 -*-
#BeautifulSoup执行流程
# ①将一段文档传入BeautifulSoup 的构造方法,就能得到一个文档的对象,可以传入一段字符串或一个文件句柄；
# ②首先,文档被转换成Unicode,并且HTML的实例都被转换成Unicode编码
# ③然后,Beautiful Soup选择最合适的解析器来解析这段文档,如果手动指定解析器那么Beautiful Soup会选择指定的解析器来解析文档
from bs4 import  BeautifulSoup
print BeautifulSoup("Sacr&eacute; bleu!")#<html><body><p>Sacré bleu!</p></body></html>

html_doc=open("TestHtml1.html").read()
soup_html=BeautifulSoup(html_doc)#使用BeautifulSoup解析这段代码,能够得到一个 BeautifulSoup 的对象
print soup_html.prettify()#按照标准的缩进格式的结构输出:

#几个简单的浏览结构化数据的方法:
print soup_html.title #完整的title标签：<title>The Dormouse's story</title>
print soup_html.title.name  #标签名称：title
print soup_html.title.string #title标签内的文本：The Dormouse's story
print soup_html.title.parent.name #title 父标签的名称 head

print soup_html.p #匹配到的第一个完整的p标签：<p class="title"><b>The Dormouse's story</b></p>
print soup_html.p['class'] #匹配到的第一个完整的p标签的class属性值，返回的是列表：['title']
# 说明：如果第一个匹配到的p标签没有class属性soup_html.p['class']这种取值方式会报错，soup_html.p.get('class')这种就不会，其实就是字典的取值方式
print soup_html.p.get('class')

print soup_html.find_all('a')#获取所有a标签，以列表的形式输出
print soup_html.find(id='link1')#关键字参数获取id='link1'的标签

#列子：获取所有a标签href属性的值
for hr in soup_html.find_all('a'):
    print hr.get('href')

print soup_html.img['src']

print soup_html.a.get_text()#获取第一个a标签的文本值
print soup_html.get_text()#获取所有文本值

#接下来讲述：对象种类
#Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .
