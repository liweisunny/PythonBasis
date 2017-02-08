# -*- coding: utf-8 -*-

#创建和使用字典
#①
py_dic={"liwei":21,"lijie":22,'lijiji':"23"}
#说明：字典由多个键及与其对应的值构成的键-值对组成，一个键值对就是字典的一项，上述例子中名字是键，年龄是值，键与值之间用：隔开，想时间用,隔开
#整个字典由一对大括号括起来，孔子点由两个大括号组成:{}。字典中键是唯一的，而值不一定唯一。
print py_dic
#②使用dict函数创建字典
items=[("name","liwei"),("age",22)]#通过其他映射（比如其他字典）或者（键，值）对的序列建立字典
d=dict(items)
print  d;
a=dict(name="lijie",age=22)#通过关键字参数创建字典
print a

#基本的字典操作
py_dic={"liwei":21,"lijie":22,'lijiji':"23"}
print len(py_dic)#返回d中的项（键-值对）的数量
py_dic["liwei"]=23#将值23关联到键“liwei”上
print py_dic["liwei"]#返回关联到键“liwei”上的值
del py_dic["lijiji"]#删除键为“lijiji”的项。
print "liwei" in py_dic#检查字典中是否含有键‘liwei’的项
# 尽管字典和列表有很多特性相同，但是也有下面一些重要的区别
# 键类型：可以使任意的不可变类型，比如浮点型、字符串、元组等。
# 自动添加：即使键起初在字典中不存在也可以为它赋值，这样字典就会建立新的项，而列表就不能将值关联到列表范围之外的的索引上
# 成员资格：表达式"liwei" in py_dic查找的是键，而不是值。而列表查找的是值而不是索引。
# 说明：在字典中检查键的成员资格比在列表中检查值的成员资格要更高效，数据结构的规模越大，两者的效率差距越明显

#字典的格式化字符串
dic={'jon':22,'bech':23,'shit':34}
str="jon's age is %(jon)s."% dic#键必须是字典中存在的
print str
template='''<html><head>
<title>%(title)s</title></head>
<body><h1>%(title)s</h1>
<p>%(text)s</p>
</body>
'''
dic={"title":"My Home page","text":"happy new day"}
print template % dic;

#字典方法

#clear() 清楚字典中的所有项，原地操作，没有返回值，或者说返回none
print  "clear方法"

d={};
d['namw']='liwei'
d['age']='22'
print  d;
d.clear();
print  d;

#使用场景
#1
x={}
y=x
x['key']='liwei'
print y
x={}
print y
#2
x={}
y=x
x['key']='liwei'
print y
x.clear()
print y

#copy方法：返回一个具有相同键值对的新字典（这个方法实现的是浅复制，因为值本身就是相同的。而不是副本）
print "copy 方法"
print "浅复制"
x={"name":"liwei","age":["22",'23']}
y=x.copy()
print y
y["name"]='lijie'#在副本中替换值是不会影响原始字典的
y["age"].remove('22')#修改某个值（原地修改而不是替换）就会影响原始字典，避免这种问题的方式就是深复制（deep copy）。
print y
print x

print "深复制"
from copy import deepcopy
x={"name":"liwei","age":["22",'23']}
y=deepcopy(x)#深复制，赋值其包含的所有的值
print y
y["name"]='lijie'
y["age"].remove('22')
print y
print x

#fromkeys 方法：使用给定的key建立新的字典，每个键默认对应的值为none
print  "fromkeys方法"
x=dict.fromkeys({"name","age"})
print x
x=dict.fromkeys({"name","age"},'(unknown)')#设置默认值
print x

#get方法：s是个更宽松的访问字典项的方法，一般来说，如果试图访问字典中不存在的项时会出错，而get不会，会返回一个None值，还可以自定义默认值。
print "get方法"
d={}
#print d["name"] 报错
print d.get('name',"liwei")
d={"name":"liwei","age":"22"}
print d.get("name","llll")#键存在的时候在设置默认值就无效了，和普通访问一样。

#has_key方法：检查字典汇总是否含有给出的键，表达式的d.has_key(k)相当于kind.
print "has_key方法"
d={}
print d.has_key("name")
d["name"]="ksd"
print d.has_key("name")
#print d.kind("name")

#items和iteritems items方法将所有字典的项以列表的形式返回，iteritems作用大致相同返回一个迭代器对象而不是列表。
print "items方法"
d={"name":"liwei","age":"22"}
print d.items()
print "iteritems方法"
obj=d.iteritems()
print obj
print list(obj)
#说明：在很多情况下使用iteritems更高效（尤其是想要迭代结果的情况下）

#keys和iterkeys   keys方法将字典中的键以列表的形式返回，而iterkeys则返回针对键的迭代器。
print "keys方法"
d={"name":"liwei","age":"22"}
print d.keys()
print "iterkeys方法"
obj=d.iterkeys()
print obj
print list(obj)

#values和itervalues   values方法将字典中的值以列表的形式返回，而itervalues则返回针对值的迭代器。
print "keys方法"
d={"name":"liwei","age":"22"}
print d.values()
print "iterkeys方法"
obj=d.itervalues()
print obj
print list(obj)

#pop方法用来获取对应于给定键的值，然后将这个键-值对从字典中移除。
print 'pop方法'
d={'x':1,'y':2}
print d.pop('x')
print d

#popitem 方法类似于list.pop，后者会移除列表的最后一个元素，但不同的是，字典是无序的，popitem移除随机项，若想一个接一个的移除并处理项，这个方法就会很有用。
print "popitem方法"
d={"name":"liwei","age":"22"}
print d.popitem()

#setdefault 方法在某种程度上类似于get方法，就是能够获得与给定键相关联的值，除此之外，setdefault还能在字典中不含有给定键的情况下设定相应的键值。
print "setdefault方法"
d={}
print d.setdefault('name','liwei')
print d
d["age"]=22
print d.setdefault("age","90")
#当键不存在的时候setdefault返回默认值并且相应的更新字典，如果键存在那么就返回与其对应的值，但不改变字典，默认值是可选的。

#update方法可以利用一个字典项更新另外一个字典
print "update方法"
d={"name":"liwei","age":"22"}
x={"age":"23"}
d.update(x)
print d









