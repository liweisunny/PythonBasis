# -*- coding: utf-8 -*-
#Tag python对象与XML或HTML原生文档中的tag相同:
from bs4 import BeautifulSoup

soup=BeautifulSoup("<b class='blosset'>Liwei is a Good Boy</b>")
tag=soup.b
print type(tag)#<class 'bs4.element.Tag'>

#Tag中的属性和方法：
#① name
print tag.name
#如果改变了tag的name,那将影响所有通过当前Beautiful Soup对象生成的HTML文档:
tag.name='bbb'
print tag #<bbb class="blosset">Liwei is a Good Boy</bbb>

#②Attributes：操作方式与字典完全一致
print tag['class'] #列表的形式返回class属性的所有值（因为存在多值属性）
print tag.get('class') #列表的形式返回class属性的所有值（因为存在多值属性）,这种形式取值，当class属性不存在的时候不会报错
print tag.attrs #字典的形式返回：{'class': ['blosset']}

tag['class']='liwei' # 修改属性值
tag['id']=123 # 添加新属性
print tag  # <bbb class="liwei" id="123">Liwei is a Good Boy</bbb>
del tag['id'] # 删除属性
print tag # <bbb class="liwei" >Liwei is a Good Boy</bbb>

#Attributes—多值属性
css_soup=BeautifulSoup("<p class='cla1 cla2'>liwei</p>")
print css_soup.p['class'] # ['cla1', 'cla2']
css_soup.p['class']=['cla1','cla2','cla3']
print css_soup # <html><body><p class="cla1 cla2 cla3">liwei</p></body></html>
#如果某个属性看起来好像有多个值,但在任何版本的HTML定义中都没有被定义为多值属性,那么Beautiful Soup会将这个属性作为字符串返回
id_soup=BeautifulSoup("<h1 id='id1 id2'>liwei</h1>")
print id_soup.h1['id']
#如果转换的文档是XML格式,那么tag中不包含多值属性
xml_soup=BeautifulSoup("<p class='cla1 cla2'>liwei</p>",'xml')
print xml_soup.p['class'] # cla1 cla2


