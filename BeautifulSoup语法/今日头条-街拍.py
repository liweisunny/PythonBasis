# -*- coding:utf-8 -*-
# 导入用到的模块
import os
import json
from pprint import pprint
from urllib import urlopen
from bs4 import BeautifulSoup

offset = 0;  # 定制偏移量
while(True):
    print offset
    #基础url
    url ='http://www.toutiao.com/search_content/?offset={offset}&format=json&keyword=%E7%BE%8E%E5%A5%B3&autoload=true&count=20&cur_tab=1'.replace('{offset}',str(offset))
    # ①
    res=urlopen(url)
    data_dic=json.loads(res.read().decode())
    data_dic=data_dic.get('data')
    if not data_dic:
        break
    #②
    article_urls=[articleurl.get('article_url')for articleurl in data_dic if articleurl.get('article_url')]
    for url in article_urls:
        #③
        soup =BeautifulSoup( urlopen(url).read(), 'html.parser')
        div_tag=soup.find('div',id='article-main')
        if not div_tag:
            continue
        photo_urls=[photo_url.get('src') for photo_url in div_tag.find_all('img') if photo_url.get('src')]
        dir_name="D://python//爬虫街拍//"+div_tag.find('h1').string+'//'#目录+文件夹名称
        #④
        for photo_url in photo_urls:
            photo_name = photo_url.rsplit('/', 1)[-1] + '.jpg'
            res=urlopen(photo_url)
            diry=dir_name+photo_name
            if not os.path.exists(dir_name):  #判断目录是否存在
                os.makedirs(dir_name)# 创建多级目录
            f=open(diry, 'wb')
            f.write(res.read())
            f.close()
    offset=offset+20

'''
①
这里我们首先通过 request.urlopen(url) 向这个 url 发送请求，返回的数据保存在 res 中，res 是一个 HttpResponse 对象，
通过调用其 read 方法获取实际返回的内容，由于 read 方法返回的是 Python 的 bytes 类型的字符串，
通过调用其 decode 方法将其编码成 string 类型字符串，默认为 UTF-8 编码。由于数据以 json 格式返回，
因此通过 json.load 方法将其转为 Python 的字典形式。
②
这里使用了列表推导式，循环文章列表，通过 get('article_url') 获取到文章的 URL，
加上 if 判断条件是为了防止因为数据缺失而得到空的文章 URL。
我们将通过不断请求这些文章的 URL，读取其内容，并把图片提取出来保存到我们的硬盘里。
③
创建BeautifulSoup对象，解析html,找到div以及div内的img标签，获取其src属性的值
④
循环请求src链接，创建目录保存图片
'''