# -*- coding: utf-8 -*-
#1.多态的应用场景
#任何不知道对象到底是什么类型，但是又要对对象“做点什么”的时候，都会用到多态。这不仅限于方法---很多内建运算符和函数都有多态的性质
#方法：绑定到对象特性上面的函数称为方法。
#例①--方法
print 'abc'.count('a')
print [1,2,'a'].count('a')

#例②--运算符
def add(x,y):
    return x+y;
print add(1,2);
print add("liwei ai ","lijie")

#例③--函数(repr()和len()多态的表现：包装各种类型并展现出来，计算不同类型的长度)
def len_message(x):
    print "The length of ",repr(x),"is",len(x);
len_message('liwei')
len_message([1,2,3])

#2.子类and超类
#当一个对象所属的类是另外一个对象所属类的子集时前者被称为后者的子类，后者则是前者的超类。

#封装：对全局作用域中其他区域隐藏多余细节的原则。听起来向多态，但封装并不等同于多态，多态可以让用户对于不知道是什么类（或对象类型）的对象进行方法调用，而封装是可以不用关心对象是如何构建的而直接进行使用。

#定义一个类
__metaclass__=type#确定使用新式类
class Person:#python中类的命名规则首字母大写，单数形式
    def setName(self,name):#self参数是对象本身，没有它的话成员方法就没法访问他们要对其特性进行操作的对象本身了。
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print 'my name is %s'%self.name
p=Person()
p1=Person()
p.setName("liwei")#这种调用方式等同于Person.setName(p,'liwei')
p.greet()#这种调用方式等同于Person.greet(p)
p1.setName("ljie")
p1.greet()

#3.方法：self参数正式方法和函数的区别，方法（更专业一点可以称为绑定方法）将它们的第一个参数绑定到所属实例上，因此这个参数可以不必提供。

#将特性绑定到一个普通函数上，这样就不会有特殊的self参数了：
class Class:
    def method(self):
        print 'I have a self'
def function():
    print "I don't..."
instance=Class()
instance.method();
instance.method=function#将方法绑定到函数上
instance.method()

#注意：self参数并不取决于调用方法的方式，目前使用的是实例调用方法，可以随意使用引用同一个方法的其他变量：
class Bird:
    song='Squaawk'
    def sing(self):
        print self.song
bird=Bird()
bird.sing()
birdsong=bird.sing#将方法绑定到变量上
birdsong()#尽管这种访问看起来与函数调用方式十分相似，但是变量birdsong引用绑定方法bird.sing上，也就意味着这还是对self参数的访问（也就是说，它仍旧绑定到类的相同实例上）

#4.私有化：为了让方法或者特性变为私有（从外部无法访问），只要在它的名字前面加上双下划线即可：
class Secretive:
    def __inaccessible(self):#在类的内部会被翻译成：_Secretive__inaccessible()
        print "Bet you can't see me"
    def accessible(self):
        print "The secret message is :"
        self.__inaccessible()
#现在__inaccessible从外界无法访问，而在类内部还可以使用
s=Secretive()
#s.__inaccessible()#私有方法访问不到
s.accessible()
#说明：类的内部定义中，所有以双下划线开始的名字都被翻译成前面加上但下划线和类名的形式，知道了这个实际上还是能在类的外部访问这些私有方法，尽管不应该这样做。
s._Secretive__inaccessible()

#5.类的命名空间
#所有位于class语句中的代码都在特殊的命名空间中执行--类命名空间，这个类命名空间可以由类内部所有成员访问，并不是所有python程序员都知道类的定义其实就是执行代码块。
class MemCount:
    members=0
    def init(self):
        MemCount.members+=1#不同于self.members
        print MemCount.members
m1=MemCount()
m1.init()#1
m2=MemCount()
m2.init()#2
print m1.members
print m2.members
m1.members='Two'
print m1.members
print m2.members
#说明：上面代码中，在类作用域内定义了一个可供所有成员（实例）访问的变量，用来计算类的成员数量，
# 新numbers值被写到了m1的特性中，屏蔽了类范围内的变量，这跟函数内部的局部和全局变量的行为的行为十分类似。

#6.指定超类
class Filter:
    def init(self):
        self.blocked=[]
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAFilter(Filter):#SPAFilter是Filter的子类
    def init(self):
        self.blocked=['SPAM']
f=Filter()
f.init()
print f.filter([1,2,3])
s=SPAFilter()
s.init()
print s.filter(['SPAM','SPAM','SPAM','SPAM','eggs','bacon','SPAM'])
#说明：Filter是个用于过滤序列的通用类，事实上它不能过滤任何东西，其用途在于它可以用作其他类的基类（超类）。
#SPAFilter定义的两个要点：①这里用提供新定义的方式重写了Filter的init定义；②filter方法的定义是从Filter类中拿过来（继承）的，所以不用重写它的定义。第二个要点揭示了继承的用处

#7 调查继承
#内建函数issubclass:查看一个类是否是另一个类的子类
print issubclass(SPAFilter,Filter)
#s属性__bases__:用于获取已知类的基类(们)
print SPAFilter.__bases__
print Filter.__bases__
#isinstance()方法：检查一个对象是否是一个类的实例(不建议使用，使用多态会更好一些)
s=SPAFilter()
print isinstance(s,SPAFilter)#true
print isinstance(s,Filter)#true
print isinstance(s,str)#false   isinstance对于类型(str)也起作用
#特性__class__：用于获取对象属于哪个类
print s.__class__

#8 多个超类
class Calculator:
    def calcalate(self,expression):
        self.value=eval(expression)
class Talker:
    def talk(self):
        print 'Hi.my value is',self.value
class TalkingCalculator(Calculator,Talker):
    pass
tc=TalkingCalculator()
tc.calcalate('1+2*3')
tc.talk()
#TalkingCalculator类继承了Calculator和Talker两个类，这种行为称为多重继承，有个需要注意的地方就是，如果一个方法从多个超类继承，也就是说继承的超类汇总有同名的方法，这时候就需要注意一下
#继承的顺序,先继承的类中的方法会重写后继承的类中的方法

#9 接口和内省
#hasattr():检查所需方法是否在对象中存在
print hasattr(tc,'talk')
#getattr函数允许提供默认值，以便特性不存在的时候使用，然后对返回的对象使用callable函数检查特性是否可调用
print callable(getattr(tc,'talk',None))
#__dict__特性用于查看对象内所有存储的值
print tc.__dict__