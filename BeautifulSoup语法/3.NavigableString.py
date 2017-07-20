# -*- coding: utf-8 -*-
# 字符串常被包含在tag内.Beautiful Soup用 NavigableString 类来包装tag中的字符串:
from bs4 import BeautifulSoup
tag=BeautifulSoup("<b class='clas1'>李伟</b>")
print tag.string # 李伟
print type(tag.string) # <class 'bs4.element.NavigableString'>

# 一个 NavigableString 字符串与Python中的Unicode字符串相同,通过 unicode() 方法可以直接将 NavigableString 对象转换成Unicode字符串
unicode_string=unicode(tag.string)
print unicode_string # 李伟
print type(unicode_string) # <type 'unicode'>

# tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用 replace_with() 方法:
tag.string='lijie'
print tag.string
tag.string.replace_with('lijiebao')
print tag.string
# 说明：NavigableString 对象支持 遍历文档树 和 搜索文档树 中定义的大部分属性, 并非全部.
# 尤其是,一个字符串不能包含其它内容(tag能够包含字符串或是其它tag),字符串不支持 .contents 或 .string 属性或 find() 方法.
# 如果想在Beautiful Soup之外使用 NavigableString 对象,需要调用 unicode() 方法,
# 将该对象转换成普通的Unicode字符串,否则就算Beautiful Soup已方法已经执行结束,该对象的输出也会带有对象的引用地址.这样会浪费内存.






