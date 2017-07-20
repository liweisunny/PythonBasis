# -*- coding:utf-8 -*-
# 修改tag的名称和属性
from bs4 import BeautifulSoup
soup=BeautifulSoup("<p><b class='class1'>liwei is a good boy</b></p>")
print soup.prettify()
tag=soup.b
tag.name='bbb' #修改标签名称
tag['class']='class_class1'# 修改class属性
tag['id']='b1' # 增加id属性
print tag
print soup.prettify() #改变的是整个文档树，并不是当前tag的值
del tag['class'] #删除class属性
print tag
print soup.prettify()

# 修改 .string
# 给tag的 .string 属性赋值,就相当于用当前的内容替代了原来的内容:
tag.string='lijie is a pig'
print tag
tag_p=soup.p
print tag_p
tag_p.string='liwei love pig'
print tag_p
# 注意: 如果当前的tag包含了其它tag,那么给它的 .string 属性赋值会覆盖掉原有的所有内容包括子tag

# append()
# Tag.append() 方法向tag中添加内容,就好像Python的列表的 .append() 方法:
soup=BeautifulSoup('<b>liwei</b>')
print soup
soup.b.append('lijie')
print soup
print soup.b.contents

# BeautifulSoup.new_string() 和 .new_tag()
# 如果想添加一段文本内容到文档中也没问题,可以调用Python的 append() 方法或调用工厂方法 BeautifulSoup.new_string() :
soup=BeautifulSoup('<b></b>')
tag=soup.b
tag.append('hello')
newstring=soup.new_string(' there')
tag.append(newstring)
print tag
print tag.contents
# 如果想要创建一段注释,或 NavigableString 的任何子类,将子类作为 new_string() 方法的第二个参数传入:
from bs4 import Comment
newstring=soup.new_string('Nice to see you',Comment)
tag.append(newstring)
print tag
print tag.contents
# 创建一个tag最好的方法是调用工厂方法 BeautifulSoup.new_tag() :
newtag=soup.new_tag("a",href="www.baidu.com")# 第一个参数作为tag的name,是必填,其它参数选填
tag.append(newtag)
print tag
newtag.string='liwei'
print tag

# insert()
# Tag.insert() 方法与 Tag.append() 方法类似,区别是不会把新元素添加到父节点 .contents 属性的最后,而是把元素插入到指定的位置
soup=BeautifulSoup('<a>liwei</a>')
soup.a.insert(0,' lijie love ')
print soup.a

# insert_before() 和 insert_after()
# insert_before() 方法在当前tag或文本节点前插入内容:
soup=BeautifulSoup('<p><b>liwei</b></p>')
tag_b=soup.b
newtag=soup.new_tag('h1')
newtag.string='lijie'
tag_b.insert_before(newtag)
print soup
tag_b.string.insert_before('lijie ai ')
print soup
# insert_after() 方法在当前tag或文本节点后插入内容:
soup=BeautifulSoup('<p><b>liwei</b></p>')
tag_b=soup.b
newtag=soup.new_tag('h1')
newtag.string='lijie'
tag_b.insert_after(newtag)
print soup
tag_b.string.insert_after(' ai lijie')
print soup

# clear() 移除当前tag的内容
soup=BeautifulSoup('<p>liwei<b>lijie</b></p>')
tag_b=soup.b
print tag_b
print soup
tag_b.clear()
print tag_b
print soup

# extract()
# PageElement.extract() 方法将当前tag移除文档树,并作为方法结果返回:
soup=BeautifulSoup("<a href='www.baidu.com'>liwei ai lijie <i>baobao1</i> <i>baobao2</i></a>")
tag_a=soup.a
print tag_a
tag_i=soup.i.extract() #存在多个的时候移除第一个匹配到的
print tag_a
print tag_i
print tag_i.parent
# 这个方法实际上产生了2个文档树: 一个是用来解析原始文档的 BeautifulSoup 对象,
# 另一个是被移除并且返回的tag.被移除并返回的tag可以继续调用 extract 方法:
string_i=tag_i.string.extract()
print string_i
print string_i.parent

# decompose() 将当前节点移除文档树并完全销毁，没有返回值
soup=BeautifulSoup("<a href='www.baidu.com'>liwei ai lijie <i>baobao1</i> <i>baobao2</i></a>")
soup.i.decompose()
print soup.a

# replace_with()
# PageElement.replace_with() 方法移除文档树中的某段内容,并用新tag或文本节点替代它:
soup=BeautifulSoup("<a href='www.baidu.com'>liwei ai lijie<i>baobao1</i></a>")
tag_a=soup.a
print tag_a
soup.i.replace_with(' and baobao')
print tag_a
# replace_with() 方法返回被替代的tag或文本节点,可以用来浏览或添加到文档树其它地方

# wrap()
# PageElement.wrap() 方法可以对指定的tag元素进行包装
# (wrap含有包装,打包的意思,但是这里的包装不是在外部包装而是将当前tag的内部内容包装在一个tag里.
# 包装原来内容的新tag依然在执行 wrap() 方法的tag内) ,并返回包装后的结果:
soup=BeautifulSoup('<p>l love lijie </p>')
print soup
soup.string.wrap(soup.new_tag('b'))# 使用b标签包装p标签内的文本
print soup
soup.p.wrap(soup.new_tag('div'))# 使用div标签包装p标签
print soup

# unwrap()
# Tag.unwrap() 方法与 wrap() 方法相反.将移除tag内的所有tag标签,该方法常被用来进行标记的解包:
markup = '<a href="http://example.com/">I linked to <i>example.com</i> <i>lijie</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a
print a_tag
a_tag.i.unwrap()# 移除标签并不移除标签内的文本,指移除匹配到的第一个
print a_tag
# 与 replace_with() 方法相同, unwrap() 方法返回被移除的tag






