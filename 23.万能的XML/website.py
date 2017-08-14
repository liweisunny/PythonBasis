# -*- coding:utf-8 -*-
from xml.sax.handler import ContentHandler
from xml.sax import parse
import os
class Dispatcher:
    '''
    调度处理程序,根据节点名称调用指定的方法，匹配不到的调用默认的方法
    '''
    def dispatch(self,prefix,element,attrs=None):
        mname=prefix+element.capitalize()
        dname='default'+prefix.capitalize()
        maction=getattr(self,mname,None)
        args = []
        if callable(maction):
            pass
        else:
            maction=getattr(self,dname,None)
            args.append(element)
        if prefix=='start':
            args.append(attrs)
        if callable(maction):
            maction(*args)
    def startElement(self,element,attrs):
        self.dispatch('start',element,attrs)
    def endElement(self,element):
        self.dispatch('end',element)

class WebsiteConstructor(Dispatcher,ContentHandler):
    '''
    xml文档处理类
    '''
    passthrough=False
    def __init__(self,directory):
        self.directory=[directory]
        self.ensureDirectory()
    def ensureDirectory(self):
        '''
        检查目录，不存在即创建
        :return:
        '''
        path=os.path.join(*self.directory)
        if not os.path.isdir(path):
            os.makedirs(path)
    def characters(self, content):
        '''
        文本处理
        :param content:
        :return:
        '''
        if self.passthrough:
            self.out.write(content)
    def defaultStart(self,name,attrs):
        '''
        默认开始节点处理方法
        :param name: 节点名称
        :param attrs:节点属性
        :return:
        '''
        if self.passthrough:
            self.out.write('<'+name)
            for key ,val in attrs.items():
                self.out.write('%s="%s"'%(key,val))
            self.out.write('>')
    def defaultEnd(self,name):
        '''
        默认结束节点处理方法
        :param name: 节点名称
        :return:
        '''
        if self.passthrough:
            self.out.write('</%s>' % name)
    def startDirectory(self,attrs):
        self.directory.append(attrs['name'])
        self.ensureDirectory()
    def endDirectory(self):
        self.directory.pop()
    def startPage(self,attrs):
        '''
        单独定义的page标签开始时的处理方法
        :param attrs: 属性
        :return:
        '''
        fielname=os.path.join(*self.directory+[attrs['name']+'.html'])
        self.out=open(fielname,'w')
        self.writeHeader(attrs['title'])
        self.passthrough=True
    def endPage(self):
        '''
        单独定义的page标签结束时的处理方法，
        :return:
        '''
        self.passthrough=False
        self.writeFooter()
        self.out.close()
    def writeHeader(self,title):
        self.out.write('<html>\n<head>\n   <title>')
        self.out.write(title)
        self.out.write('</title>\n</head>\n <body>\n')
    def writeFooter(self):
        self.out.write('\n </body>\n</html>\n')
parse('website.txt',WebsiteConstructor('public_html'))
