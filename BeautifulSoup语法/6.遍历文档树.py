# -*- coding: utf-8 -*-
from  bs4 import BeautifulSoup
soup=BeautifulSoup(open("TestHtml1.html").read())
# 子节点
# 一个Tag可能包含多个字符串或其它的Tag,这些都是这个Tag的子节点.Beautiful Soup提供了许多操作和遍历子节点的属性.
# 注意: Beautiful Soup中字符串节点不支持这些属性,因为字符串没有子节点

#tag的名字
# 操作文档树最简单的方法就是告诉它你想获取的tag的name.如果想获取 <head> 标签,只要用 soup.head :
print soup.head
print soup.title
print soup.body.a #获取body标签中的第一个a标签
print soup.a # 获取整个文档对象中的第一个a标签
print soup.find_all('a') # 获取所有a标签以列表的形式输出

# .contents 和 .children
# tag的 .contents 属性可以将tag的子节点以列表的方式输出:
head_tag=soup.head
print head_tag # <head><title>The Dormouse's story</title></head>
print head_tag.contents # [<title>The Dormouse's story</title>]
title_tag=head_tag.contents[0]
print title_tag # <title>The Dormouse's story</title>
print title_tag.contents # [u"The Dormouse's story"]
# BeautifulSoup 对象本身一定会包含子节点,也就是说<html>标签也是 BeautifulSoup 对象的子节点:
print len(soup.contents)
print soup.contents[0].name
# 字符串没有 .contents 属性,因为字符串没有子节点:
title_string=title_tag.contents
print title_string
# print title_string[0].contents # 报错：AttributeError: 'NavigableString' object has no attribute 'contents'
# 通过tag的 .children 生成器,可以对tag的子节点进行循环:
for t in soup.find("a",id='link1').children:
    print repr(t)

#.descendants
# 说明：.contents 和 .children 属性仅包含tag的直接子节点.例如,<head>标签只有一个直接子节点<title>
print type(head_tag.descendants) # <type 'generator'>
print type(head_tag.children) # <type 'listiterator'>
print type(head_tag.contents) # <type 'list'>
print head_tag.contents
# 但是<title>标签也包含一个子节点:字符串 “The Dormouse’s story”,这种情况下字符串 “The Dormouse’s story”也属于<head>标签的子孙节点.
# .descendants 属性可以对所有tag的子孙节点进行递归循环
for t in head_tag.descendants:
    print t
print len(list(head_tag.children)) # 1
print len(list(head_tag.descendants)) # 2

#.string
# 如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点:
print title_tag.string # The Dormouse's story
print title_tag.contents # [u"The Dormouse's story"]
# 如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同:
print head_tag.contents # [<title>The Dormouse's story</title>]
print head_tag.string # The Dormouse's story
print title_tag.string # The Dormouse's story
# 如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None :
print soup.html.string # None

# .strings 和 stripped_strings
# 如果tag中包含多个字符串 ,可以使用 .strings 来循环获取:
for string in soup.strings:
    print (repr(string))
# 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容,全部是空格的行会被忽略掉,段首和段末的空白会被删除.
for string in soup.stripped_strings:
    print repr(string)

# 父节点
# 继续分析文档树,每个tag或字符串都有父节点:被包含在某个tag中，通过 .parent 属性来获取某个元素的父节点.
print title_tag # <title>The Dormouse's story</title>
print title_tag.parent #<head><title>The Dormouse's story</title></head>
print type(title_tag.parent) # <class 'bs4.element.Tag'>
# 文档title的字符串也有父节点:<title>标签
print title_tag.string # The Dormouse's story
print title_tag.string.parent # <title>The Dormouse's story</title>
print type(title_tag.string.parent) # <class 'bs4.element.Tag'>
# 文档的顶层节点比如<html>的父节点是 BeautifulSoup 对象:
print type(soup.html.parent) # <class 'bs4.BeautifulSoup'>
# BeautifulSoup 对象的 .parent 是None:
print soup.parent #None
# 通过元素的 .parents 属性可以递归得到元素的所有父辈节点
for parent in soup.a.parents:
    if parent is None:
        print parent
    else:
        print parent.name

# 兄弟节点
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
print(sibling_soup.prettify())
# 同一个元素的子节点(意思是指父节点一定要相同),可以被称为兄弟节点.一段文档以标准格式输出时,兄弟节点有相同的缩进级别。上述中<b>和<c>可以被称为兄弟节点
# 在文档树中,使用 .next_sibling 和 .previous_sibling 属性来查询兄弟节点:
print sibling_soup.b.next_sibling # <c>text2</c>
print sibling_soup.c.previous_sibling # <b>text1</b>
# <b>标签有 .next_sibling 属性,但是没有 .previous_sibling 属性,因为<b>标签在同级节点中是第一个.同理,<c>标签有 .previous_sibling 属性,却没有 .next_sibling 属性:
print sibling_soup.b.previous_sibling # None
print sibling_soup.c.next_sibling # None
# 例子中的字符串“text1”和“text2”不是兄弟节点,因为它们的父节点不同:
print sibling_soup.b.string # text1
print sibling_soup.b.string.next_sibling # None
# 实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白,看看“TestHtml1.html”文档:
'''
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
'''
# 如果以为第一个<a>标签的 .next_sibling 结果是第二个<a>标签,那就错了,真实结果是第一个<a>标签和第二个<a>标签之间的顿号和换行符:
print soup.a # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print soup.a.next_sibling # ,
# 第二个<a>标签是顿号的 .next_sibling 属性:
print soup.a.next_sibling.next_sibling #<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# 通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出:
for a_nex in soup.a.next_sibling:
    print repr(a_nex)
for a_pre in soup.find(id='link3').previous_sibling:
    print repr(a_pre)

# 回退和前进
'''
<html><head><title>The Dormouse's story</title></head>
<p class="title"><b>The Dormouse's story</b></p>
'''
# HTML解析器把这段字符串转换成一连串的事件: “打开<html>标签”,”打开一个<head>标签”,”打开一个<title>标签”,
# ”添加一段字符串”,”关闭<title>标签”,”打开<p>标签”,等等.Beautiful Soup提供了重现解析器初始化过程的方法.
# .next_element 和 .previous_element
# .next_element 属性指向解析过程中下一个被解析的对象(字符串或tag),结果可能与 .next_sibling 相同,但通常是不一样的.
last_a=soup.find("a",id='link3')
print last_a # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
print last_a.next_sibling # ; and they lived at the bottom of a well.
print last_a.next_element # Tillie
# 说明：文档被解析成树形结构,所以下一步解析过程应该是当前节点的子节点
# .previous_element 属性刚好与 .next_element 相反,它指向当前被解析的对象的前一个解析对象:
print last_a.previous_element # and 它的前一个解析对象
# 通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样:
print type(last_a.previous_elements)# <type 'generator'>
for a_ele in last_a.next_elements:
    print repr(a_ele)




