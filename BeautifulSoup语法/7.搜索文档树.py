# -*- coding: utf-8 -*-
# Beautiful Soup定义了很多搜索方法,这里着重介绍2个: find() 和 find_all() .其它方法的参数和用法类似。
from  bs4 import  BeautifulSoup
soup=BeautifulSoup(open('TestHtml1.html').read())
# 过滤器
# 介绍 find_all() 方法前,先介绍一下过滤器的类型(过滤器只能作为搜索文档的参数,或者说应该叫参数类型更为贴切,原文中用了 filter 因此翻译为过滤器) ,
# 这些过滤器贯穿整个搜索的API.过滤器可以被用在tag的name中,节点的属性中,字符串中或他们的混合中.

# 过滤器-字符串
# 最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<b>标签:
print soup.find_all('b')

# 过滤器-正在表达式
# 如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.
import re
for tag in soup.find_all(re.compile('^b')):#打印以b开头的标签名字
    print tag.name
print soup.find_all(re.compile('t'))# 会输出所有包含t的标签以及标签中的内容
for tag in soup.find_all(re.compile('t')): # 打印包含t的标签的名字
    print tag.name

# 过滤器-列表
# 如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签:
print soup.find_all(['a','b'])

# 过滤器-True
# True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
for tag in  soup.find_all(True):
    print tag.name

# 过滤器-方法
# 如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数（元素参数,HTML文档中的一个tag节点,不能是文本节点） ,
# 如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False
#例①
def checkTag(tag):# 自定义一个方法过滤器，用来筛选包含class属性但不包含id属性的元素
    return tag.has_attr('class') and not tag.has_attr('id')
for tag in soup.find_all(checkTag):
    print tag
#例②
print ''
from bs4 import NavigableString
def search_string(tag): #查找当前元素的前后解析对象都是字符串的元素
    return (isinstance(tag.next_element,NavigableString) and isinstance(tag.previous_element,NavigableString))
for tag in soup.find_all(search_string):
    print tag

# 搜索方法的细节 find_all( name , attrs , recursive , text , **kwargs )
# find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
print soup.find_all('title')
print soup.find_all('p','title')
print soup.find_all('a')
print soup.find_all(id='link2')
import re
print soup.find_all(text=re.compile('sisters'))
# 有几个方法很相似,还有几个方法是新的,参数中的 text 和 id 是什么含义?
# 为什么 find_all("p", "title") 返回的是CSS Class为”title”的<p>标签? 我们来仔细看一下 find_all() 的参数

# name参数
# name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉.
print soup.find_all('title')
# 重申: 搜索 name 参数的值可以使用任一类型的 过滤器 ,字符窜,正则表达式,列表,方法或是 True .

# keyword参数
# 如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,
# 如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性.
print soup.find_all(id='link1')
# 如果传入 href 参数,Beautiful Soup会搜索每个tag的”href”属性:
print soup.find_all(href=re.compile('elsie'))
# 搜索指定名字的属性时可以使用的参数值有： 字符串 , 正则表达式 , 列表, True .
# 例
print soup.find_all(id=True)# 找所有包含 id 属性的tag,无论 id 的值是什么
# 使用多个指定名字的参数可以同时过滤tag的多个属性:
print soup.find_all(href=re.compile('elsie'),id='link1')
# 有些tag属性在搜索时不能使用,比如HTML5中的 data-* 属性
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
# print data_soup.find_all(data-foo="value")
# 但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
print data_soup.find_all(attrs={"data-foo": "value"})# 这种方式同样适用于其他属性

# 按CSS搜索
# 按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,
# 使用 class 做参数会导致语法错误.从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag:
print soup.find_all('a',class_='sister')
# class_ 参数同样接受不同类型的 过滤器 ,字符串,正则表达式,方法或 True :
print soup.find_all(class_=re.compile('itl'))

def class_action(css_class):
    return css_class is not None and len(css_class)==6
print soup.find_all(class_=class_action)
# tag的 class 属性是 多值属性 .按照CSS类名搜索tag时,可以分别搜索tag中的每个CSS类名:
css_soup=BeautifulSoup('<p class="body strike"></p>')
print css_soup.find_all(class_='strike')
print css_soup.find_all(class_='body strike')
print css_soup.find_all(class_=class_action)

# text参数
# 通过 text 参数可以搜索文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True
print soup.find_all(text="Elsie")
# [u'Elsie']
print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']
print soup.find_all(text=re.compile("Dormouse"))
#[u"The Dormouse's story", u"The Dormouse's story"]
def is_the_only_string_within_a_tag(s):
    return (s == s.parent.string)
print soup.find_all(text=is_the_only_string_within_a_tag)
# [u"The Dormouse's story", u"The Dormouse's story", u'Elsie', u'Lacie', u'Tillie', u'...']
print soup.find_all('a',text='Elsie')# 查找文本值为Elsie的a标签

# limit参数
# find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,
# 可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.
print soup.find_all('a',limit=2)# 返回最先搜索到的两个a标签

# recursive参数
# 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
print soup.find_all('title')# [<title>The Dormouse's story</title>]
print soup.find_all('title',recursive=False)#[]

# 像调用 find_all() 一样调用tag
# find_all() 几乎是Beautiful Soup中最常用的搜索方法,所以我们定义了它的简写方法.
# BeautifulSoup 对象和 tag 对象可以被当作一个方法来使用,这个方法的执行结果与调用这个对象的 find_all() 方法相同
# 下面两行代码是等价的:
print soup.find_all('title')
print soup('title')
# 下面两行代码是等价的:
print soup.title.find_all(text=True)
print soup.title(text=True)

# find()
# find( name , attrs , recursive , text , **kwargs )
# find_all() 方法将返回文档中符合条件的所有tag,尽管有时候我们只想得到一个结果.比如文档中只有一个<body>标签,
# 那么使用 find_all() 方法来查找<body>标签就不太合适, 使用 find_all 方法并设置 limit=1 参数不如直接使用 find() 方法.
# 下面两行代码是等价的:
print soup.find_all('title',limit=1)
print soup.find('title')
# 唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果.
# find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None .
print soup.find_all('tite',limit=1)#[]
print soup.find('tite')# None
# soup.head.title 是 tag的名字 方法的简写.这个简写的原理就是多次调用当前tag的 find() 方法:
print soup.head.title
print soup.find('head').find('title')

# find_parents() 和 find_parent()
# find_parents( name , attrs , recursive , text , **kwargs )
# find_parent( name , attrs , recursive , text , **kwargs )
# 我们已经用了很大篇幅来介绍 find_all() 和 find() 方法,Beautiful Soup中还有10个用于搜索的API.
# 它们中的五个用的是与 find_all() 相同的搜索参数,另外5个与 find() 方法的搜索参数类似.区别仅是它们搜索文档的不同部分.
# 记住: find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等.
# find_parents() 和 find_parent() 用来搜索当前节点的父辈节点,搜索方法与普通tag的搜索方法相同,搜索文档搜索文档包含的内容.
a_string=soup.find(text='Elsie')
print a_string
print a_string.find_parent()# 搜索父节点
print a_string.find_parents('a')# 搜索所有a标签父辈节点
print a_string.find_parents('p',class_='story')
print a_string.find_parents('p',class_='title') #[]
# find_parent() 和 find_parents() 方法会让人联想到 .parent 和 .parents 属性.它们之间的联系非常紧密.
# 搜索父辈节点的方法实际上就是对 .parents 属性的迭代搜索。

# find_next_siblings() 合 find_next_sibling()
# find_next_siblings( name , attrs , recursive , text , **kwargs )
# find_next_sibling( name , attrs , recursive , text , **kwargs )
# 这2个方法通过 .next_siblings 属性对当前tag的所有后面解析的兄弟tag节点进行迭代,
# find_next_siblings() 方法返回所有符合条件的后面的兄弟节点, find_next_sibling() 只返回符合条件的后面的第一个tag节点.
first_link=soup.a
print first_link
print first_link.find_next_siblings('a')
first_story_p=soup.find('p','story')
print first_story_p
print first_story_p.find_next_sibling('p')

# find_previous_siblings() 和 find_previous_sibling()
# find_previous_siblings( name , attrs , recursive , text , **kwargs )
# find_previous_sibling( name , attrs , recursive , text , **kwargs )
# 这2个方法通过 .previous_siblings 属性对当前tag的前面解析 的兄弟tag节点进行迭代,
# find_previous_siblings() 方法返回所有符合条件的前面的兄弟节点, find_previous_sibling() 方法返回第一个符合条件的前面的兄弟节点:
last_link=soup.find('a',id='link3')
print last_link
print last_link.find_previous_sibling('a')
print last_link.find_previous_siblings('a')

# find_all_next() 和 find_next()
# find_all_next( name , attrs , recursive , text , **kwargs )
# find_next( name , attrs , recursive , text , **kwargs )
# 这2个方法通过 .next_elements 属性对当前tag的之后的tag和字符串进行迭代,(但与next_element不同)
# find_all_next() 方法返回所有符合条件的节点, find_next() 方法返回第一个符合条件的节点:
first_link=soup.a
print first_link
print first_link.find_all_next(text=True)
print first_link.find_next('p')
print first_link.find_next()
print first_link.next_element

# find_all_previous() 和 find_previous()
# find_all_previous( name , attrs , recursive , text , **kwargs )
# find_previous( name , attrs , recursive , text , **kwargs )
# 这2个方法通过 .previous_elements 属性对当前节点前面的tag和字符串进行迭代,
# find_all_previous() 方法返回所有符合条件的节点, find_previous() 方法返回第一个符合条件的节点.
first_link=soup.a
print first_link
print first_link.find_previous('title')
print first_link.find_all_previous('p')

# CSS选择器
# Beautiful Soup支持大部分的CSS选择器 [6] ,在 Tag 或 BeautifulSoup 对象的 .select() 方法中传入字符串参数,即可使用CSS选择器的语法找到tag:
print soup.select('title')
print soup.select('p:nth-of-type(3)')# :nth-of-type(n) 选择器匹配属于父元素的特定类型的第 N 个子元素的每个元素.n 可以是数字、关键词或公式。# 通过tag标签逐层查找:
print soup.select('body a')
print soup.select('html head title')
# 找到某个tag标签下的直接子标签()
print soup.select('head > title')
print soup.select('p > a')
print soup.select('p > a:nth-of-type(2)') # 查找p标签直接子节点中的第二个a标签
print soup.select('p > #link1')
print soup.select('body > a')
# 通过CSS的类名查找:
print soup.select('.sister')
print soup.select('[class~=sister]')     #没有~也可以
# 通过tag的id查找:
print soup.select('#link1')
print soup.select('a#link2')
# 通过是否存在某个属性来查找:
print soup.select('a[href]')
# 通过属性的值来查找:
print soup.select('a[href="http://example.com/elsie"]')
print soup.select('a[href^="http://example.com/"]') #以http://example.com/开头
print soup.select('a[href$="tillie"]')         #以tillie结尾
print soup.select('a[href*=".com/el"]')    # 包含.com/el
# 通过语言设置来查找:
multilingual_markup = """
 <p lang="en">Hello</p>
 <p lang="en-us">Howdy, y'all</p>
 <p lang="en-gb">Pip-pip, old fruit</p>
 <p lang="fr">Bonjour mes amis</p>
"""
multilingual_soup = BeautifulSoup(multilingual_markup)
print multilingual_soup.select('p[lang|=en]')