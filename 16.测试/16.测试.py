# -*- coding: utf-8 -*-
# 测试工具
# ① doctest:简单的一些模块，检查文档用的，但对于编写单元测试也很在行
# ② unitest: 通用测试框架

# doctest
#if __name__=='__main__':
    #import doctest,Square
    #doctest.testmod(Square,verbose=True)

# unitest
import unittest,ADD
class AddTestCase(unittest.TestCase):
    def testIntergers(self):
        for x in xrange(-10,10):
            for y in xrange(-10,10):
                p=ADD.add(x,y)
                self.failUnless(p==x+y,'Inter multiplication faild')

    def testFloats(self):
        for x in xrange(-10, 10):
         for y in xrange(-10, 10):
             x=x/10.0
             y=y/10.0
             p = ADD.add(x, y)
             self.failUnless(p == x + y, 'Float multiplication faild')
if __name__=='__main__':
    unittest.main() # 负责运行测试。它会实力化所有TestCase的子类，运行所有名字以test开头的方法
# 如果定义了叫做starUp和tearDown的方法，它们就会在运行每个测试方法之前和之后执行，
# 这样就可以使用这些方法为所有测试提供一般的初始化和清理代码，这呗称为测试夹具。


