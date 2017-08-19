# -*- coding:utf-8 -*-
# 创建html页面
from xml.sax.handler import ContentHandler
from xml.sax import parse
class PageMaker(ContentHandler):
    passthrough=False;
    def startElement(self, element, attrs):
        if element=='page':
            self.passthrough=True
            self.out=open(attrs['name']+'.html','w')
            self.out.write('<html><head>\n')
            self.out.write('<title>%s</title>\n'%attrs['title'])
            self.out.write('</head><body>\n')
        elif self.passthrough:
            self.out.write('<'+ element)
            for key ,val in attrs.items():
                self.out.write('%s="%s"'%(key,val))
            self.out.write('>')
    def endElement(self, element):
        if element=='page':
            self.passthrough=False
            self.out.write('</body></html>\n')
            self.out.close()
        elif self.passthrough:
            self.out.write('</%s>'%element)
    def characters(self, content):
        if self.passthrough:
            self.out.write(content)
parse('website.txt',PageMaker())
