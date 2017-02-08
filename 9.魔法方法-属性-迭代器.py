# -*- coding: utf-8 -*-
# 1.构造方法
#说明：构造方法类似于以前使用过的名为init的初始化方法，当一个对象创建后，会立即调用构造方法。
#创建方式：把init名字修改为魔法版本的 __init__即可
#例①
class Foobar:
    def __init__(self):
        self.somvar=42
f=Foobar()
print f.somvar
#例②带参数的构造方法
class Foobar:
    def __init__(self,value=42):
        self.somvar=value
f=Foobar('liwei is a bug shuai ge')
print f.somvar

# 1.1 重写一般方法和特殊的构造方法
#例①
class A:
    def hellow(self):
        print 'my name is A'
class B(A):
    pass
a=A();
b=B();
a.hellow()
b.hellow()
#说明：B类继承A类，所以继承了A类中的方法，因为B类没有自己的hello方法，所以当hello被调用时，原始信息就被打印出来了。
class B(A):
    def hellow(self):#重写父类中的hellow方法
        print 'my name is B'
b=B();
b.hellow()

#重写构造方法时需要注意一些，如果一个类的构造方法被重写，那么就需要调用超类（你所继承的类）的构造方法，否则对象可能不会被正确地初始化。
#例②
class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print 'Aaah...'
            self.hungry=False;
        else:
            print 'No thanks'
b=Bird()
b.eat()
b.eat()

class SongBird(Bird):
    def __init__(self):
        self.sound='Squawk'
    def sing(self):
        print  self.sound
sb=SongBird()
sb.sing()
#SongBird继承了Bird类，所以它也有eat方法。但是当调用eat方法的时候事情发生了。。
#sb.eat(),,出错了，为什么呢，因为我们没有调用超类的构造方法，构造方法在子类中被重写了，没有初始化hungry 属性。so子类的构造方法必须调用超类的构造方法，
#解决这种问题有两种方式：①调用超类构造方法的未绑定版本；②使用super函数

# 1.2 调用未绑定的超类构造方法
#例①
class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)#未绑定方法调用案例
        self.sound='Squawk'
    def sing(self):
        print self.sound

sb=SongBird()
sb.sing()
sb.eat()
sb.eat()

#说明：在调用一个实例的方法时，该方法的self参数会被自动绑定到实例上，这称为绑定方法，例如：sb.sing()，这种调用方式；
#但如果直接调用类的方法（比如： Bird.__init__），那么就没有实例会被绑定。这样就可以自由地提供需要的self参数，这样的方法称为未绑定方法。
# 通过将当前的实例作为self参数提供给未绑定方法，SongBird就能够使用启超类构造方法的所有实现，也就是说属性hungry能被设置。

# 1.3 使用super函数（只能在新式类中使用）---推荐
# 例①
__metaclass__=type#确定使用新式类
class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print 'Aaah...'
            self.hungry=False;
        else:
            print 'No thanks'

class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()#super函数使用：当前类和对象可以作为super函数的参数使用，调用函数返回的对象的任何方法都是调用超类的方法，而不是当前类的方法。
        self.sound='Squawk'
    def sing(self):
        print  self.sound
sb=SongBird()
sb.sing()
sb.eat()
sb.eat()

# 2. 成员访问
#2.1 基本的序列和映射规
#例①
def checkIndex(key):#检查索引的类型以及索引是否是大于0的正整数
    if not isinstance(key,(int,long)):raise TypeError
    if key<0:raise IndexError
class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        self.start=start
        self.step=step
        self.changed={}
    def __getitem__(self, key):
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start+key*self.step
    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key]=value
    #def __delitem__(self, key):
        #del self.changed[key]
s=ArithmeticSequence(1,2)
print s[4]#相当于调用__getitem__方法
s[4]=2#相当于调用__setitem__方法
print s[4]
#del s[4]
#print s[4]
print s[5]
#说明：上述实现了一个算术数列，序列中的每个元素都比它前面的元素大一个常数，用户能通过名为changed方法将特例规则保存在字典中，从而修改一些元素的值，如果元素没有被修改，那就计算self.start+key*self.step的值，上述并没有实现__del__方法 ，so 当调用 del s[4] 是会报错的.
#在这里我们是用来isinstance函数（这个函数应该尽量避免使用，因为类或类型检查和python中多态的目标背道而驰）， 因为Python语言中明确规定索引必须是整数，遵守标准是使用类型检查（很少的）正当理由。

# 2.2 子类化列表，字典和字符串
#如果只想在一个操作中自定义行为，那么其他的方法就不用实现，这就是程序员的懒惰（也是常识）
#注意：如果类的行为和默认的行为很接近这就很有用，如果需要重新实现大部分方法，那么还不如重新写一个类
#当子类化一个内键类型---比如list的时候，也就间接地将object子类化了，因此的类就自动成为新式类，这就意味着可以使用像suoer函数这样的特性了。
#例 ①
class Counterlist(list):
    def __init__(self,*args):
        super(Counterlist,self).__init__(*args)
        self.counter=0
    def __getitem__(self, index):
        self.counter+=1
        return super(Counterlist,self).__getitem__(index)
cl=Counterlist(range(10))
print cl
cl.reverse()
print cl
del cl[3:6]
print cl
print cl[4]+cl[2]
print cl.counter

# 2.3 属性
#定义：通过访问器定义的特性被称为属性。
#例①
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setSize(self,size):
        self.width,self.height=size
    def getSize(self):
        return self.width,self.height
r=Rectangle()
r.width=10
r.height=5
print r.getSize()
r.setSize((150,100))
print r.width
# 在上面的例子中，getSzie和setSize方法一个名为size的假想特性的访问器方法，size是由width和height构成的元组。
# 读者可以随意使用一些更有趣的方法替换这里的函数，例如计算面积或者 对角线长度这些代码没错，但是却有缺陷。‘当程序使用这个类的时候不应该还要考虑它是怎么实现的（封装）。
# 如果有一天要改变类的实现，将size变成一个真正的特性，这样width和height就可以动态的算出，那么就要把它们放到一个访问器方法中去，并且任何使用这个类的程序都必须重写。
# 客户代码（使用代码的代码）应该能用同样的方式对待所有特性。
# 那么如何解决上述问题？把所有的特性都放到访问器方法中？这当然没问题。但如果有很多简单的特性，那么就很不现实了（有点笨）。如果那样做就得写很多访问器方法，
# 它们除了返回或者设置特性就不做任何事了。’复制和粘贴式或切割代码式的编程方式显然是很糟糕的‘，幸好python能隐藏访问器方法，让所有特性看起来一样。’这些通过访问器定义的特性被称为属性‘。
# 实际上python中有两种创建属性的机制。我主要讨论的机制---只在新式类中使用的property函数。
#例②
__metaclass__=type
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def setSize(self,size):
        self.width,self.height=size
    def getSize(self):
        return self.width,self.height
    size=property(getSize,setSize)
r=Rectangle()
r.width=20
r.height=10
print r.size
r.size=100,50
print r.width,r.height
#很明显，size特性仍然取决于getSize和setSize中的计算。但他们看起来就像普通的属性一样
# 实际上，property函数可以用0、1、2、3、4个参数来调用。如果没有参数，产生的属性既不可读也不可写。如果只有一个参数调用（取值方法），产生的属性是只读的，
# 第三个参数（可选）是一个用于删除特性的方法。第四个参数（可选）是一个文档字符串。property的四个参数分别被叫做fget ,fset ,fdel 和doc--
# 如果想要一个属性是只写的，并且有文档字符串，能使用他们的关键字参数。





