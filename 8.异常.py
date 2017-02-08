# -*- coding: utf-8 -*-
# 一.引发异常：可以使用一个类（应该是内建Expection异常类的子类）或者实例参数调用raise语句。使用类时程序会自动创建实例
#例①
#raise Exception#引发一个没有热河有关错误信息的普通异常
#raise Exception('myself ex')#自定义错误信息引发异常
#例②导入异常模块，使用dir函数列出模块中的所有内建异常类
import exceptions
print dir(exceptions)#异常类列表，所有的异常类都可以使用raise语句,Expection是所有异常类的基类
#raise ArithmeticError
print ("%s    %s")%('Exception','        所有异常类的基类')
print ("%s    %s")%('AttributeError','   特性引用或赋值失败时引发')
print ("%s    %s")%('IOError','          试图打开不存在文件（包括其他情况）时引发')
print ("%s    %s")%('IndexError','       在使用程序列中不存在的索引是引发')
print ("%s    %s")%('KeyError','         在使用映射中不存在的键时引发')
print ("%s    %s")%('NameError','        在找不到名字（变量）时引发')
print ("%s    %s")%('SyntaxError','      在代码为错误形式时引发')
print ("%s    %s")%('TypeError','        在内建操作或者函数应用于错误类型的对象时引发')
print ("%s    %s")%('ValueError','       在内建操作或者函数应用于正确类型的对象，但是该对象使用不合适的值时引发')
print ("%s    %s")%('ZeroDivisionError','在除法或者模除操作的第二个参数为0时引发')

# 二.自定义异常
class MyException(Exception):#继承异常基类
    pass
'''
# 三.捕捉异常（try/expect）
#例①
try:
    x=input('enter first num: ')
    y=input('enter second num: ')
    print x/y
except ZeroDivisionError:#指定捕捉的异常类型为ZeroDivisionError，其他类型的异常不会捕捉到，可以不指定这样就会捕捉到所有异常
    print "the second num can't be zero"
#例②
class Calculator:
    isopen=False;#屏蔽机制，控制是否捕捉异常
    def calc(self,expr):
        try:
            return eval(expr)
        except:
            if self.isopen:
                print 'Division by zero is illegal'
            else:
                raise#捕捉到异常，又想重新引发异常，使用不带参数的raise
calculator=Calculator()
print calculator.calc('10/2')
calculator.isopen=True;
print calculator.calc('10/0')

# 四.不止一个except字句
try:
    x=input('enter first num: ')
    y=input('enter second num: ')
    print x/y
except ZeroDivisionError:#指定捕捉的异常类型为ZeroDivisionError，其他类型的异常不会捕捉到
    print "the second num can't be zero"
except TypeError:#指定捕捉的异常类型为TypeError，其他类型的异常不会捕捉到
    print "That wasn't number. was it?"

# 五.用一个块捕捉多个异常
try:
    x=input('enter first num: ')
    y=input('enter second num: ')
    print x/y
except (ZeroDivisionError,NameError,TypeError):#使用元组作为参数列出多个异常
    print "Your number was bogus"



# 六.捕捉对象（打印相应异常）
try:
    x = input('enter first num: ')
    y = input('enter second num: ')
    print x / y
except (ZeroDivisionError, NameError, TypeError),e:  # 使用元组作为参数列出多个异常
    print e

# 七.异常+ 循环+ 条件语句
while True:#当没有异常发生的时候跳出循环
    try:
        x = input('enter first num: ')
        y = input('enter second num: ')
        value=x/y;
        print 'x/y is ',value
    except Exception ,e:#出现异常循环执行
        print 'Invalid input：%s\r\nplease try again'%e
    else:
        break#执行成功跳出异常

# 八 最后.....finally
#finally :用来确保某些代码不管异常是否发生都会被执行（清理代码）。它和try字句联合使用
x=None#在这里给x赋值的原因是因为，如果try语句中发生异常，这样x就没有值，finally语句中del x就会出现异常
try:
    x=1/0
finally:
    print 'clear....'
    del x #这句话执行完以后x就不存在了
#执行上述代码时无论程序是否发生异常finally块都会被执行，一旦程序异常，x值也会在程序崩溃之前清理掉了。
'''
# 九.异常和函数
#异常在函数内引发而不被处理，它就会传播至函数调用的地方，如果在函数调用的地方也没有处理异常，它就会继续传播，一直到达主程序（全局作用域），
# 如果那里也没有处理异常，程序会带着堆栈跟踪终止。
#例①
def faulty():
    raise Exception('Something is wrong...')
def ignore_exception():
    faulty()
def handle_exception():
    try:
        faulty()
    except:
        print 'Exception handle...'
handle_exception()
#说明：可以看到，faulty中产生的异常通过faulty和ignore_exception传播，最终导致了堆栈跟踪。它传播到handle_exception，在这个函数里面被处理掉了。











