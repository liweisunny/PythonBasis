# -*- coding:utf-8 -*-
# 用reportLab画图
from reportlab.lib import colors
from reportlab.graphics.shapes import  *
from reportlab.graphics import renderPDF
d=Drawing(100.100)# 创建指定大小的图纸
s=String(50,50,'Hello,Word!',textAnchor='middle')# 创建图形元素
d.add(s)
renderPDF.drawToFile(d,'hello.pdf','A simple PDF file') #将元素添加到图纸中去

# 构造折线
# reportLab针对这个需求有特定的类：PolyLine，它把坐标列表作为第一个参数。列表形式是[(x0,y0),(x1,y1),(x2,y2),....]

# 编写原型
# 构造数据源
data=[
    #Year month  pred  high   low
    (2007,8,113.2,114.2,112.2),
    (2007,9,112.8,115.8,109.8),
    (2007,10,111.0,116.0,106.0),
    (2007,11,109.8,116.8,102.8),
    (2007,12,107.3,115.5,99.3),
    (2008,1,105.2,114.2,96.2),
    (2008,2,104.1,114.1,94.1),
    (2008,3,99.9,110.9,88.9),
    (2008,4,94.8,106.8,82.8),
    (2008,5,91.2,104.2,78.2)]
drawing=Drawing(200,150)
pred=[row[2]-40 for row in data]
high=[row[3]-40 for row in data]
low=[row[4]-40 for row in data]
times=[200*((row[0]+row[1]/12.0)-2007)-110 for row in data]
drawing.add(PolyLine(zip(times,pred),strokeColor=colors.blue))
drawing.add(PolyLine(zip(times,high),strokeColor=colors.red))
drawing.add(PolyLine(zip(times,low),strokeColor=colors.green))
drawing.add(String(65,115,'Sunspots',fontSize=18,fillColor=colors.red))
renderPDF.drawToFile(drawing,'report1.pdf','Sunspots')