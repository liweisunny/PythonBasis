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

#2.4 静态方法和类成员方法
#说明：静态方法和类成员方法在创建时分别被装入Staticmethod类型和Classmethod类型的对象中。静态方法的定义没有self参数，且能够被类本身调用。
# 类方法在定义时需要名为cls的参数，类似于self参数，类成员方法可以直接用类的具体对象调用。但cls参数是自动被绑定到类的
#例①
__metaclass__=type
class MyClass:
    def smeth():
        print 'this is a static method'
    smeth=staticmethod(smeth)
    def cmeth(cls):
        print 'this is a class method of',cls
    cmeth=classmethod(cmeth)
# 例②
# 例①中手动包装和替换方法的方式有点单调，可以使用一种叫装饰器的新语法定义静态方法和类成员方法；使用@操作符将装饰器列出，从而指定一个或者多个装饰器（多个装饰器在应用时的顺序与指定顺序相反）。
__metaclass__=type
class MyClass:
    @staticmethod
    def smeth():
        print 'this is a static method'
    @classmethod
    def cmeth(cls):
        print 'this is a class method of',cls
MyClass.smeth()
MyClass.cmeth()
my=MyClass()
my.cmeth()
my.smeth()
#说明：静态方法和类成员方法在python中并不是向来都很重要，主要原因是大部分情况下可以使用函数或者绑定方法代替。在早期的版本中没有得到支持也是一个原因。但即使看不到两者在当前代码中的大量应用，也不要忽视静态方法和类成员方法的应用（比如工厂函数），可以好好的考虑一下使用新技术。

# 2.5 拦截对象的所有特性访问
# __getattribute__(self,name):当特性name被访问时自动被调用（只能在新式类中使用）
# __getattr__(self,name):当特性name被访问且对象没有相应的特性时被调用。
# __setatrr__(self,name,value):当试图给特性name赋值时会被自动调用。
# __delatrr__(self,name):当试图删除特性name时被自动调用
#例①
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def __setattr__(self, name, value):
        if name=='size':
            self.width,self.height=value
        else:
            self.width,self.height=value
    def __getattr__(self, name):
        if name=='size':
            return self.width,self.height
        else:
            raise AttributeError

#说明
#__setattr__方法在所涉及到的特性不是size时也会被调用。因此，这个方法必须把两方
#面都考虑进去:如果属性是size，那么就像前面那样执行操作，否则就要使用特殊方法
#__dict__，该特殊方法包含一个字典，字典里面是所有实例的属性。为了避免setattr
#方法被再次调用(这样会使程序陷入死循环)，dict方法被用来代替普通的特性赋值
#操作。

#_getattr_方法只在普通的特性没有被找到的时候调用，这就是说如果给定的名字不是
#size，这个特性不存在，这个方法会引发一个AttrlbuteError异常。如果希望类和hasattr
#或者是ge七a七tr这样的内建函数一起正确地工作，}gera七七r_方法就很重要。如果使用的
#是size属性，那么就会使用在前面的实现中找到的表达式。

#就像死循环陷阱和_setattr_有关系一样，还有一个陷阱__getattribute__有关系.
#因__getattribute-拦截所有特性的访问(在新式类中)，也拦截对_dict_的访问!访
#问__getattribute__中与Self相关的特性时:使用超类__getattribute_方法(使用super函数)是唯一安全的途径。

# 2.6迭代器
# 到目前为止只是在for循环中对序列和字典进行迭代，但实际上也能对其他的对象进行迭代：实现_iter_方法的对象。

# __iter__方法返回一个迭代器(iterator)，所谓的迭代器就是具有next方法(这个方法在调用时不需要任何参数)的对象。在调用next方法时，迭代器会返回它的下一个值。如果next方法被调用，但迭代器没有值可以返回，就会引发一个StopIteration异常。

# 迭代器规则在Python 3.0中有一些变化。在新的规则中，迭代器对象应该实现__next__方法，而不是next。而新的内建函数next可以用于访问这个方法。换句话说next(it)等同于3.0之前版本中的it.next(),

# 正式的说法是，一个实现了iter方法的对象是可迭代的，一个实现了next方法的对象则是迭代器。

#例①
class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):
        self.a,self.b=self.b,self.b+self.a
        return self.a
    def __iter__(self):
        return self;

fibs=Fibs();
for f in fibs:#每次迭代实际上就是调用next方法
    if f>1000:
        print f;
        break;#不设置break会一直循环下去
    else:
        print f

#内建函数iter可以从可迭代的对象中获得迭代器。
it=iter([1,2,37])
it.next()
it.next()
#除此之外，它也可以从函数或者其他可调用对象中获取可迭代对象

#从迭代器得到序列
#除了在迭代器和可迭代对象上进行迭代(这是经常做的)外，还能把它们转换为序列。在大部分能使用序列的情况下(除了在索引或者分片等操作中)，能使用迭代器(或者可迭代对象)替换。
# 关于这个的一个很有用的例子是使用list构造方法显式地将迭代器转化为列表。
class TestIterator:
    value=0
    def next(self):
        self.value+=1
        if self.value>10:raise StopIteration
        return self.value
    def __iter__(self):
        return self;
tt=TestIterator();
print list(tt)

# 2.7 生成器
#生成器是一种用普通函数语法定义的迭代器。
#例①
nested=[[1,2,3],[3,4,2],['liwei','lijie','libo']]
def flatten(nested):
    for sublist in nested:
        for item in sublist:
            yield item
#说明：这里的yield语句是新知识。任何包含yield语句的函数称为生成器。这就在于它不是想return那样返回值，而是每次产生多个值。
# 每次产生一个值（使用yield）语句，函数就会被冻结：即函数停在那点等待被激活。函数被激活后就从停止的那点开始执行。
for num in flatten(nested)        :
    print num
print list(flatten(nested))

#生成器推导式：和列表式推导式不同的是外层是()小括号而不是[]中括号，
#场景：如果希望将可迭代对象（例如生成大量的值）“打包”，那么最好不要使用列表推导式，因为它会立即实例化一个列表，从而丧失迭代的优势
g=((i+2)**2 for i in range(2,27))
print g.next()#16
print list(g)
#更奇妙的地方在于生成器推倒式可以在当前圆括号内直接使用，例如在函数调用中，不用增加另外一对圆括号，如下：
print sum(i**2 for i in range(10))

# 2.8 递归生成器
#处理多层嵌套
#例①
def flatten(nested):
    try:
        for sublist in nested:
            for num in flatten(sublist):
                yield num
    except TypeError:
        yield nested
nested = [[1, 2, 3], 4, [5, 6, 7], 8, [[9, 10, 11], 12, 13]]
print list(flatten(nested))
#说明：
# 当flatten被调用时，有两种可能性(处理递归时大部分都是有两种情况):基本情况和需要递归的情况。
# 在基本的情况中，函数被告知展开一个元素(比如一个数字)，这种情况下，for循环会引发一个TypeError异常(因为试图对一个数字进行迭代)，生成器会产生一个元素。
# 如果展开的是一个列表(或者其他的可迭代对象)，那么就要进行特殊处理。程序必须遍历所有的子列表(一些可能不是列表)，并对它们调用flatten。
# 然后使用另一个for循环来产生被展开的子列表中的所有元素。这可能看起来有点不可思议，但却能工作。

#例①存在一个问题，如果nested是一个类似于字符串的对象，那么它就是一个序列不会引发TypeError。
# 为了处理这种情况，则必须在生成器的开始处添加一个检查语句。试着将传人的对象和一个字符串拼接，看看会不会出现TypeError，
# 这是检查一个对象是不是似类于字符串的最简单、最快速的方法。下面是加人了检查语句的生成器:
#例②
def flatten(nested):
    try :
        #不要迭代类似字符串的对象
        try:nested + ''#数字加字符串的时候回引发TypeError
        except TypeError :pass
        else:raise  TypeError#当nested是字符串的时候自己引发一个TypeError
        for sublist in nested:
             for num in flatten(sublist):
                    yield num
    except TypeError:
        yield nested
nested=[[1,2,3],4,['liwei',6,7],'lijie',[[9,10,11],12,13]]
print list(flatten(nested))

#2.9 通用生成器
# 生成器定义：
# 生成器是一个包含yield关键字的函数。当它被调用时，在函数体中的代码不会被执行，而会返回一个迭代
# 器。每次请求一个值，就会执行生成器中的代码，直到遇到一个yield或者return语句。yield语句意味着应该生成一个值。
# return语句意味着生成器要停止执行(不再生成任何东西，return语句只有在一个生成器中使用时才能进行无参数调用)。
# 换句话说，生成器是由两部分组成:生成器的函数和生成器的迭代器。生成器的函数是用def语句定义的，包含y}eld的部分，
# 生成器的迭代器是这个函数返回的部分。按一种不是很准确的说法，两个实体经常被当做一个，合起来叫做生成器。
#举例说明：
def simple_generator():
    yield 1
print simple_generator #<function simple_generator at 0x0304F130>函数
print simple_generator() #<generator object simple_generator at 0x03047C88>迭代器

#2.10 生成器方法
# 生成器的新属性(在Python 2.5中引入)是在开始运行后为生成器提供值的能力。表现为生成器和“外部世界”进行交流的渠道，要注意下面两点：
# ① 外部作用域访问生成器的send方法，就像访问next方法一样，只不过前者使用一个参数(要发送的“消息”---任意对象)。
# ② 在内部则挂起生成器，yield现在作为表达式而不是语句使用，换句话说，当生成器重新运行的时候，yield方法返回一个值，也就是外部通过send方法发送的值。
#    如果next方法被使用，那么yield方法返回None，注意，使用Send方法(而不是next方法)只有在生成器挂起之后才有意义(也就是说yield函数第一次被执行之后)。
#    如果在此之前需要给生成器提供更多信息，那么只需使用生成器函数的参数。如果针对刚刚启动的生成器使用send方法，那么可以将None作为参数进行调用。
#举例说明：
def repeater(value):
    while True:
        new=(yield value)#为了安全起见在使用返回值的时候，闭合yield表达式
        if new is not None:
            value=new

r=repeater(42)
print r.next() #42
print r.send('liwei')#必须在yield函数第一次被执行之后使用或者传None，否则会引发异常

# 生成器还有其他两个方法(在Python 2.5及以后的版本中):
# 口throw方法(使用异常类型调用，还有可选的值以及回溯对象)用于在生成器内引发一个异常(在yield表达式中)。
# 口close方法(调用时不用参数)用于停止生成器。close方法(在需要的时候也会由Python垃圾收集器调用)也是建立在异常的基础上的。
# 它在yield运行处引发一个GeneratorExit异常，所以如果需要在生成器内进行代码清理的话，则可以将yield语句放在try/finally语句中。
# 如果需要的话，还可以捕捉GeneratorExit异常，但随后必需将其重新引发(可能在清理之后)、引发另外一个异常或者直接返回。
# 试着在生成器的close方法被调用后再通过生成器生成一个值则会导致RuntimeError异常。

#2.11 模拟生成器
# 生成器在旧版本的Python中是不可用的。下面介绍的就是如何使用普通的函数模拟生成器。
# 先从生成器的代码开始。首先将下面语句放在函数体的开始处: result=[]
# 如果代码已经使用了。result这个名字，那么应该用其他名字代替(使用一个更具描述性的名字是一个好主意)，
# 然后将这种形式的代码: yield some_expression 用这种语句:result.append(some_expression)替换;
# 最后，在函数的末尾添加这条语句:return result
# 尽管这个版本可能不适用于所有生成器，但对大多数生成器来说是可行的(比如，它不能用于一个无限的生成器，当然不能把它的值放人列表中)。

# 举例：flatten生成器用普通的函数重写
def flatten(nested):
    result = []
    try:
        try: nested+''
        except TypeError:pass
        else:raise TypeError
        for sublist in nested:
            for item in flatten(sublist):
                result.append(item)
    except TypeError:
        result.append(nested)
    return result;
nested=[[1,2,3],4,['liwei',6,7],'lijie',[[9,10,11],12,13]]
print flatten(nested)

#2.12八皇后问题
#判断冲突的函数
def conflict(state,nextX):
    nextY=len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True;
    return False
#conflict((2,3),5)
# 说明：state是已知皇后的位置（元组的形式），nextY代表下一个皇后的水平位置（x坐标或列），netxY代表垂直位置（y坐标或行），
# 如果下一个皇后和前面的皇后有同样的水平位置，或者是在一条对角线上，就会发生冲突，接着返回true,如果没有冲突就返回false。
# abs(state[i]-nextX) in (0,nextY-1) 这个表达式的意思如果下一个皇后和正在考虑的前一个皇后的水平距离为0（列相同），
# 或者等于垂直距离（在一条对角线上）就返回true,否则返回false。

# 递归生成器解决八皇后问题
def queens(num=8,state=()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state)==num-1:
                yield (pos,)
            else:
                for result in queens(num,state+(pos,)):
                    yield (pos,)+result

print list(queens(3))
print list(queens(4))
for solution in queens(8):
    print solution
print len(list(queens(8)))

#2.13 打包
def prettyprint(solution):
    def line(pos,length=len(solution)):
        return '. '*(pos)+'X '+'. '*(length-pos-1)
    for pos in solution:
        print line(pos)
import random
prettyprint(random.choice(list(queens(8))))