# -*- coding: utf-8 -*-
#条件语句
#False   None    0     ''    ()     []     {}     这几种值在作为布尔表达式时会被看做假；换句话说也就是标准值False和None所有类型的数字0（包括浮点型、长整形和其他类型）、空序列（比如空字符串、元组、列表）以及空字典都为假。
print bool(False)
print bool(None)
print bool(0)
print bool('')
print bool(())
print bool([])
print bool({})
print True==1
print False==0
#使用案列 输入一个姓名，判断姓名是否包含liwei,包含的话输出 hello liwei ,you are very good ! 否则判断是否包含lijie,包含的话输出hello lijie ,you are very good !,否则输出，error!!!
name=raw_input("your name is :")
if name.endswith('liwei'):
    print "hello liwei ,you are very good !"
elif name.endswith('lijie'):
    print "hello lijie ,you are very good !"
else:
    print "error!!"


#比较运算符
print "---------------------------------------------------------------------------------------"
print "============表达式==============================描述===================================="
print "---------------------------------------------------------------"
print "============x==y================================x等于y=================================="
print "============x<y=================================x小于y=================================="
print "============x>y=================================x大于y=================================="
print "============x>=y================================x大于等于y=============================="
print "============x<=y================================x小于等于y=============================="
print "============x!=y================================x不等于y================================"
print "============x is y==============================x和y是同一个对象========================="
print "============x is not y==========================x和y是不同对象==========================="
print "============x in y==============================x是y容器中的成员========================="
print "============x not in y==========================x不是y容器中的成员======================="
print "----------------------------------------------------------------------------------------"
#说明：只有在x和y类型相同或者近似类型的时候比较才有意义，例如两个整形或者一个整形和一个浮点形进行比较是可以的，一个整形和一个字符串比较是没有意义的。
#列子
x=y=[1,2,3]
z=[1,2,3]
print x==y
print x==z
print x is y
print  x is z
#显然，两个列表值相等但是不等同。使用==运算符来判断两个对象是否相等，使用is判定两者是否等同（同一个对象）。
#字符串和序列的比较，字符串可以按照字母的顺序排列进行比较
print 'abc'<'bac'
print [1,2]<[2,1]
print [1,[2,5]]<[1,[2,6]]
#bool运算符，and运算符就是所谓的布尔元素符，它连接两个布尔值，并且在两者都为真时返回真，否则返回假，与它同类的还有两个运算符，or和not，使用这3个运算符就可以随意结合真值。
#短路逻辑（惰性求值）：表达式x and y，需要两个都为真时才会返回真，so 如果x为假，表达式就会立刻返回False，而不管y的值，实际上，如果x为假，表达式就会返回x的值，否则返回y的值这种行为称为短路逻辑。在表达式 x or y中，x为真是返回x的值，否则返回y的值。
# a if b else c  :如果b为真，返回a的值，否则返回c的值。

#断言：条件语句的近亲，用来去报程序中的某个条件一定为真才能让程序正常工作，使用assert实现。
age=1
assert 0<age<10,'age is error'


