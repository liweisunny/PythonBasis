# -*- coding:utf-8 -*-
#from urllib import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF
#url='https://github.com/liweisunny/PythonBasis/blob/Dev/data.txt'
COMMENT_CHARS='#:'
drawing=Drawing(400,200)
data=[]
datasource=open('data.txt').readlines()
for line in datasource:
    if not line.isspace() and not line[0] in COMMENT_CHARS:
        data.append([float(n) for n in line.split(',')])
pred=[row[2] for row in data]
high=[row[3] for row in data]
low=[row[4] for row in data]
timws=[row[0]+row[1]/12.0 for row in data]
lp=LinePlot()
lp.x=50
lp.y=50
lp.height=125
lp.width=300
lp.data=[zip(timws,pred),zip(timws,high),zip(timws,low)]
lp.lines[0].strokeColor=colors.blue
lp.lines[1].strokeColor=colors.red
lp.lines[2].strokeColor=colors.green
drawing.add(lp)
drawing.add(String(250,150,'Sunspots',fontSize=14,fillColor=colors.red))
renderPDF.drawToFile(drawing,'report2.pdf','Sunspots')
