# -*- coding:utf-8 -*-
# 处理程序超类
class Handler:
    def callback(self,prefix,name,*args):
        method=getattr(self,prefix+name,None)
        if callable(method):
            return method(*args)
    def start(self,name):
        return self.callback(self,'start_'+name)
    def end(self, name):
        return self.callback(self, 'end_' + name)
    def sub(self,name):# 返回替换函数
        def substiution(match):
            result=self.callback('sub_',name,match)
            if result is None:
                return match.group(0)
            return result
        return substiution
# ① callback方法负责在给定一个前缀（比如:start_）和一个名字（比如:paragraph）后查找正确的方法，
# 并且使用getatrr获取对象，不存在则返回None；使用callable判断方法是否可以被调用，
# python3.0以后不存在callable方法，可以使用try except代替


class HTMLRenderer(Handler):
    '''
     用于生成html的具体处理程序，
     HTMLRenderer内的方法都可以通过超类处理程序的start()、end()和sub()方法来访问，
     它们实现了用于HTML文档的基本标签
    '''
    def start_document(self):
        print '<html><head><titlt>...</title></head><body>'
    def end_document(self):
        print '</body></html>'
    def start_paragraph(self):
        print '<p>'
    def end_paragraph(self):
        print '</p>'
    def start_heading(self):
        print '<h2>'
    def end_heading(self):
        print '</h2>'
    def start_list(self):
        print '<ul>'
    def end_list(self):
        print '</ul>'
    def start_listitem(self):
        print '<li>'
    def end_listitem(self):
        print '</li>'
    def start_title(self):
        print '<h1>'
    def end_title(self):
        print '</h1>'
    def sub_emphasis(self,match):
        return '<em>%s<em>'%(match.group(1))
    def sub_url(self,match):
        return '<a href="%s">%s</a>'%(match.group(1),match.group(1))
    def sub_mail(self,match):
        return '<a href="mailto:%s">%s</a>'%(match.group(1),match.group(1))
    def feed(self,data):
        print data