# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
# 格式化输出
# prettify() 方法将Beautiful Soup的文档树格式化后以Unicode编码输出,每个XML/HTML标签都独占一行
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
print soup.prettify()
# BeautifulSoup 对象和它的tag节点都可以调用 prettify() 方法:
print soup.a.prettify()

# 压缩输出
# 如果只想得到结果字符串,不重视格式,那么可以对一个 BeautifulSoup 对象或 Tag 对象使用Python的 unicode() 或 str() 方法:
print str(soup)
print unicode(soup.a)
# str() 方法返回UTF-8编码的字符串,可以指定 编码 的设置.

# 输出格式
# Beautiful Soup输出是会将HTML中的特殊字符转换成Unicode,比如“&lquot;”:
soup = BeautifulSoup("&ldquo;Dammit!&rdquo; he said.")
print unicode(soup) # =print soup
# 如果将文档转换成字符串,Unicode编码会被编码成UTF-8.这样就无法正确显示HTML特殊字符了:
print str(soup)

# get_text()
# 如果只想得到tag中包含的文本内容,那么可以调用 get_text() 方法,这个方法获取到tag中包含的所有文版内容包括子孙tag中的内容,
# 并将结果作为Unicode字符串返回:
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup)
print soup.get_text()
print soup.i.get_text()
# 可以通过参数指定tag的文本内容的分隔符:
print soup.get_text("|")
# 还可以去除获得文本内容的前后空白:
print soup.get_text("|", strip=True)
# 或者使用 .stripped_strings 生成器,获得文本列表后手动处理列表:
texts=[text for text in soup.stripped_strings]
print texts